"""Price Correlation Study page (Business Requirement 1)."""
import streamlit as st


def page_correlation_study_body():
    st.header("Price Correlation Study")
    st.info(
        "**Placeholder.** Visualises how car attributes correlate with price "
        "(correlation + PPS, plus per-variable plots). "
        "Answers Business Requirement 1 and Pass criterion 4.1."
    )
    st.write("TODO: correlation heatmap, PPS, scatter/box plots + interpretations.")
