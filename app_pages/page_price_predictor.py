import streamlit as st
import pandas as pd
from src.data_management import load_clean_data, load_price_pipeline


def page_price_predictor_body():
    df = load_clean_data()
    pipe = load_price_pipeline()
    feature_cols = [c for c in df.columns if c != "price"]

    st.title("Predict Sale Price")
    st.caption(
        "Business Requirement 2 — enter a car's details to get an estimated sale price."
    )

    c1, c2 = st.columns(2)
    with c1:
        manufacturer = st.selectbox("Manufacturer", sorted(df["manufacturer"].unique()))
        models = sorted(df[df["manufacturer"] == manufacturer]["model"].unique())
        model = st.selectbox("Model", models)
        transmission = st.selectbox("Transmission", sorted(df["transmission"].unique()))
        fuel_type = st.selectbox("Fuel type", sorted(df["fuelType"].unique()))
    with c2:
        year = st.number_input(
            "Registration year",
            min_value=int(df["year"].min()), max_value=int(df["year"].max()),
            value=int(df["year"].median()), step=1,
        )
        mileage = st.number_input(
            "Mileage",
            min_value=0, max_value=int(df["mileage"].max()),
            value=int(df["mileage"].median()), step=1000,
        )
        engine_size = st.number_input(
            "Engine size (litres)",
            min_value=float(df["engineSize"].min()), max_value=float(df["engineSize"].max()),
            value=float(df["engineSize"].median()), step=0.1,
        )
        mpg = st.number_input(
            "MPG",
            min_value=float(df["mpg"].min()), max_value=float(df["mpg"].max()),
            value=float(df["mpg"].median()), step=1.0,
        )
        tax = st.number_input(
            "Road tax (£)",
            min_value=int(df["tax"].min()), max_value=int(df["tax"].max()),
            value=int(df["tax"].median()), step=5,
        )

    if st.button("Predict sale price", type="primary"):
        row = {
            "manufacturer": manufacturer, "model": model, "year": year,
            "transmission": transmission, "mileage": mileage, "fuelType": fuel_type,
            "tax": tax, "mpg": mpg, "engineSize": engine_size,
        }
        input_df = pd.DataFrame([row])[feature_cols]
        prediction = pipe.predict(input_df)[0]
        st.markdown("---")
        st.metric("Estimated sale price", f"£{prediction:,.0f}")
        st.caption(
            "On unseen cars the model is on average within about £1,500 of the actual "
            "price (test MAE), so treat this as a strong guide rather than an exact figure."
        )
