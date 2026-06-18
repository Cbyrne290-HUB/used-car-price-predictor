import streamlit as st
from src.data_management import load_clean_data


def page_summary_body():
    df = load_clean_data()

    st.title("🚗 Used Car Price Predictor")
    st.caption(
        "A pricing tool for a used-car dealership — understand what drives value, "
        "then price any car in seconds."
    )

    c1, c2, c3 = st.columns(3)
    c1.metric("Cars analysed", f"{len(df):,}")
    c2.metric("Manufacturers", df["manufacturer"].nunique())
    c3.metric(
        "Price range",
        f"£{df['price'].min():,.0f} – £{df['price'].max():,.0f}",
    )

    st.markdown("---")

    st.subheader("The problem")
    st.markdown(
        "Pricing used stock by hand is slow and inconsistent: overprice a car and it sits on "
        "the forecourt; underprice it and margin is lost. This app learns from "
        f"**{len(df):,} real UK used-car listings** so the sales team can value vehicles "
        "quickly and consistently, and understand *why* a car is worth what it is."
    )

    st.subheader("What it does")
    st.info(
        "**Business Requirement 1 — Understand the market.** "
        "The dealership wants to know which attributes most affect a car's price. "
        "The **Price Correlation Study** page answers this with interactive visualisations."
    )
    st.info(
        "**Business Requirement 2 — Predict a price.** "
        "The dealership wants an estimated sale price for a specific car. "
        "The **Predict Sale Price** page does this live from a trained machine-learning model."
    )

    st.subheader("The data")
    st.markdown(
        "The dataset is a public-domain (CC0) collection of UK used-car listings sourced from "
        "Kaggle, covering nine manufacturers: Audi, BMW, Ford, Hyundai, Mercedes, Skoda, "
        "Toyota, Vauxhall and Volkswagen. After cleaning, each row describes one car by:"
    )
    st.markdown(
        "- **manufacturer** and **model**\n"
        "- **year** of registration\n"
        "- **mileage** (miles)\n"
        "- **transmission** and **fuelType**\n"
        "- **engineSize** (litres), **mpg**, road **tax**\n"
        "- **price** (£) — the value the model learns to predict"
    )

    with st.expander("Preview the data"):
        st.dataframe(df.head(20), use_container_width=True)

    st.markdown(
        "Full documentation — dataset, methodology and deployment — is in the "
        "project README on GitHub."
    )
