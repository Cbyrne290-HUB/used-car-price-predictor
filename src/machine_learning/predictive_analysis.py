"""Prediction helpers used by the Predict Sale Price dashboard page."""
import pandas as pd


def predict_price(input_df: pd.DataFrame, pipeline) -> float:
    """Run one row through the saved pipeline and return the predicted price."""
    prediction = pipeline.predict(input_df)
    return float(prediction[0])
