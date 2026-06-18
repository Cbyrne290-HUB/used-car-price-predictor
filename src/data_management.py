import streamlit as st
import pandas as pd
import joblib


@st.cache_data
def load_clean_data():
    """Load the cleaned used-car dataset (cached)."""
    return pd.read_csv("outputs/datasets/cleaned/used_cars_cleaned.csv")


@st.cache_resource
def load_price_pipeline():
    """Load the trained price-prediction pipeline (cached)."""
    return joblib.load("outputs/ml_pipeline/predict_price/v1/pipeline.pkl")
