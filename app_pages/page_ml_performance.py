import streamlit as st
import pandas as pd
import plotly.express as px
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error
from src.data_management import load_clean_data, load_price_pipeline


@st.cache_data
def _performance():
    df = load_clean_data()
    pipe = load_price_pipeline()
    X = df.drop(columns=["price"])
    y = df["price"]
    X_tr, X_te, y_tr, y_te = train_test_split(X, y, test_size=0.2, random_state=42)
    res = {}
    for name, Xs, ys in [("Train", X_tr, y_tr), ("Test", X_te, y_te)]:
        pred = pipe.predict(Xs)
        res[name] = {
            "r2": r2_score(ys, pred),
            "mae": mean_absolute_error(ys, pred),
            "rmse": mean_squared_error(ys, pred) ** 0.5,
            "actual": ys.reset_index(drop=True),
            "pred": pd.Series(pred),
        }
    feat = [
        n.split("__", 1)[-1]
        for n in pipe.named_steps["preprocessor"].get_feature_names_out()
    ]
    imp = pipe.named_steps["model"].feature_importances_
    params = pipe.named_steps["model"].get_params()
    return res, feat, imp, params


def page_ml_performance_body():
    res, feat, imp, params = _performance()

    st.title("ML Model Performance")
    st.caption(
        "How well the price model predicts — on the data it learned from (train) "
        "versus cars it has never seen (test)."
    )

    st.subheader("Success metric")
    st.markdown(
        "The agreed target was to explain at least **80% of price variance "
        "(R² ≥ 0.80)** on unseen cars."
    )
    if res["Test"]["r2"] >= 0.80:
        st.success(f"**Met.** Test R² = {res['Test']['r2']:.3f}.")
    else:
        st.error(f"Not met. Test R² = {res['Test']['r2']:.3f}.")

    st.subheader("Scores")
    for name in ["Train", "Test"]:
        st.markdown(f"**{name} set**")
        m1, m2, m3 = st.columns(3)
        m1.metric("R²", f"{res[name]['r2']:.3f}")
        m2.metric("Mean error (MAE)", f"£{res[name]['mae']:,.0f}")
        m3.metric("RMSE", f"£{res[name]['rmse']:,.0f}")
    st.caption(
        "The small gap between train and test scores shows the model generalises "
        "well rather than memorising the training data."
    )

    st.subheader("Actual vs predicted price")
    st.markdown("Points on the red line are perfect predictions.")
    plot_cols = st.columns(2)
    for col, name in zip(plot_cols, ["Train", "Test"]):
        actual = res[name]["actual"]
        pred = res[name]["pred"]
        idx = actual.sample(min(3000, len(actual)), random_state=42).index
        plot_df = pd.DataFrame(
            {"Actual": actual.loc[idx].values, "Predicted": pred.loc[idx].values}
        )
        fig = px.scatter(
            plot_df, x="Actual", y="Predicted", opacity=0.4, title=name,
            labels={"Actual": "Actual price (£)", "Predicted": "Predicted price (£)"},
        )
        top = float(max(plot_df["Actual"].max(), plot_df["Predicted"].max()))
        fig.add_shape(
            type="line", x0=0, y0=0, x1=top, y1=top,
            line=dict(color="red", dash="dash"),
        )
        col.plotly_chart(fig, use_container_width=True)

    st.subheader("What drives the predictions")
    imp_df = (
        pd.DataFrame({"feature": feat, "importance": imp})
        .sort_values("importance")
    )
    fig_imp = px.bar(
        imp_df, x="importance", y="feature", orientation="h",
        labels={"importance": "Importance", "feature": ""},
    )
    st.plotly_chart(fig_imp, use_container_width=True)

    st.subheader("Model and tuning")
    st.markdown(
        "The model is an **Extra Trees Regressor**, chosen after comparing it against a "
        "decision tree, random forest and gradient boosting. It was tuned with "
        "`GridSearchCV` across **six hyperparameters, three values each**. Best settings:"
    )
    keys = [
        "n_estimators", "max_depth", "max_leaf_nodes",
        "min_samples_leaf", "min_samples_split", "max_features",
    ]
    st.markdown("\n".join([f"- **{k}** = {params[k]}" for k in keys]))
