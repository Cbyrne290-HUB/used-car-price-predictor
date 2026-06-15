"""Regression evaluation helpers (used in the modelling notebook & dashboard)."""
import numpy as np
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score


def regression_performance(y_true, y_pred) -> dict:
    """Return the key regression metrics as a dictionary."""
    return {
        "R2": r2_score(y_true, y_pred),
        "MAE": mean_absolute_error(y_true, y_pred),
        "RMSE": np.sqrt(mean_squared_error(y_true, y_pred)),
    }
