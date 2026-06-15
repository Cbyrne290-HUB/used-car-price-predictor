"""Predict Sale Price page (Business Requirement 2 - live ML prediction)."""
import streamlit as st


def page_price_predictor_body():
    st.header("Predict a Car's Sale Price")
    st.info(
        "**Placeholder.** Interactive widgets feed the trained ML pipeline to "
        "predict a price live. "
        "Answers Business Requirement 2 and Pass criteria 4.2 / 5.4."
    )
    st.write("TODO: input widgets -> pipeline.predict() -> show predicted price.")
