import streamlit as st
import plotly.express as px
from src.data_management import load_clean_data


def page_correlation_study_body():
    df = load_clean_data()

    st.title("Price Correlation Study")
    st.caption(
        "Business Requirement 1 — understand which car attributes most affect price."
    )

    numeric = ["year", "mileage", "tax", "mpg", "engineSize", "price"]
    sample = df.sample(min(3000, len(df)), random_state=42)

    # --- Plot 1: correlation heatmap ---
    st.subheader("How the numeric features relate")
    st.markdown(
        "Spearman correlation (handles non-linear, monotonic relationships). "
        "Red is positive, blue is negative."
    )
    corr = df[numeric].corr(method="spearman")
    fig_heat = px.imshow(
        corr, text_auto=".2f", aspect="auto",
        color_continuous_scale="RdBu_r", zmin=-1, zmax=1,
    )
    st.plotly_chart(fig_heat, use_container_width=True)
    st.info(
        "**year** has the strongest positive link with price, and **mileage** the "
        "strongest negative one. Note year and mileage are themselves strongly related "
        "(older cars have done more miles)."
    )

    # --- Plot 2: median price by year (line) ---
    st.subheader("Price by registration year")
    by_year = df.groupby("year")["price"].median().reset_index()
    fig_year = px.line(
        by_year, x="year", y="price", markers=True,
        labels={"year": "Registration year", "price": "Median price (£)"},
    )
    st.plotly_chart(fig_year, use_container_width=True)

    # --- Plot 3: average price by manufacturer (bar) ---
    st.subheader("Average price by manufacturer")
    by_make = (
        df.groupby("manufacturer")["price"].mean().sort_values().reset_index()
    )
    fig_make = px.bar(
        by_make, x="price", y="manufacturer", orientation="h",
        labels={"price": "Average price (£)", "manufacturer": ""},
    )
    st.plotly_chart(fig_make, use_container_width=True)

    # --- Plot 4: interactive feature explorer (scatter / box) ---
    st.subheader("Explore any feature against price")
    feature = st.selectbox(
        "Choose a feature",
        [c for c in df.columns if c != "price"],
    )
    if df[feature].dtype == "object":
        fig_feat = px.box(
            df, x=feature, y="price",
            labels={"price": "Price (£)"},
        )
    else:
        fig_feat = px.scatter(
            sample, x=feature, y="price", opacity=0.4,
            labels={"price": "Price (£)"},
        )
    st.plotly_chart(fig_feat, use_container_width=True)
    st.caption(
        "Scatter plots use a 3,000-car sample so the chart stays responsive; "
        "box plots use all cars."
    )

    # --- findings ---
    st.subheader("What this tells the dealership")
    st.markdown(
        "- **Year and mileage** are the biggest numeric levers on price.\n"
        "- **Transmission** matters a lot: automatics and semi-autos sell far higher "
        "than manuals.\n"
        "- **Engine size** has a clear positive effect; **mpg** a mild negative one "
        "(economy cars are cheaper).\n"
        "- These same features dominate the prediction model — see the ML pages."
    )
