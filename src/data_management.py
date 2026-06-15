"""Helpers for loading data and the trained ML pipeline into the dashboard."""
import joblib
import pandas as pd
import streamlit as st


@st.cache_data
def load_cleaned_data(
    path: str = "outputs/datasets/cleaned/used_cars_cleaned.csv",
) -> pd.DataFrame:
    """Load the cleaned dataset used across the dashboard pages."""
    return pd.read_csv(path)


def load_pipeline(path: str):
    """Load a saved scikit-learn pipeline (.pkl) from a versioned outputs folder."""
    return joblib.load(path)
