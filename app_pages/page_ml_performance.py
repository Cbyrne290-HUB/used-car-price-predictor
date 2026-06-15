"""ML Model Performance page (model evaluation on the dashboard)."""
import streamlit as st


def page_ml_performance_body():
    st.header("ML Model Performance")
    st.info(
        "**Placeholder.** Shows pipeline steps, feature importance, and "
        "performance (R2 + Actual vs Predicted, train & test), with a clear "
        "statement on whether the success metric was met. "
        "Answers Pass criteria 4.2 / 5.2 and Merit 5.7."
    )
    st.write("TODO: train/test R2, Actual vs Predicted plots, feature importance.")
