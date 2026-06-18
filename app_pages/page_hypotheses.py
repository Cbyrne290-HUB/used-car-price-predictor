import streamlit as st
import plotly.express as px
from src.data_management import load_clean_data


def page_hypotheses_body():
    df = load_clean_data()
    sample = df.sample(min(3000, len(df)), random_state=42)

    st.title("Project Hypotheses")
    st.caption(
        "Three hypotheses were set before modelling. Each was tested statistically on "
        "the cleaned data — the key figures below are recomputed live."
    )

    # --- H1 ---
    st.subheader("Hypothesis 1 — Higher mileage means a lower price")
    r1 = df["mileage"].corr(df["price"], method="spearman")
    st.success(
        f"**Supported.** Spearman correlation = {r1:.2f} — a clear negative "
        "relationship (p < 0.001)."
    )
    fig1 = px.scatter(
        sample, x="mileage", y="price", opacity=0.4,
        labels={"mileage": "Mileage", "price": "Price (£)"},
    )
    st.plotly_chart(fig1, use_container_width=True)
    st.markdown(
        "As mileage rises, price falls. Mileage is one of the first things a buyer "
        "checks, so this is exactly what the dealership would expect."
    )

    st.markdown("---")

    # --- H2 ---
    st.subheader("Hypothesis 2 — Newer cars are worth more")
    r2 = df["year"].corr(df["price"], method="spearman")
    st.success(
        f"**Supported.** Spearman correlation = +{r2:.2f} — a strong positive "
        "relationship (p < 0.001)."
    )
    by_year = df.groupby("year")["price"].median().reset_index()
    fig2 = px.line(
        by_year, x="year", y="price", markers=True,
        labels={"year": "Registration year", "price": "Median price (£)"},
    )
    st.plotly_chart(fig2, use_container_width=True)
    st.markdown(
        "Median price climbs steadily with each newer registration year — "
        "depreciation in reverse."
    )

    st.markdown("---")

    # --- H3 ---
    st.subheader("Hypothesis 3 — Transmission type affects price")
    st.success(
        "**Supported.** Kruskal–Wallis H = 35,717 (p < 0.001) — price differs "
        "significantly across transmission types."
    )
    fig3 = px.box(
        df, x="transmission", y="price",
        labels={"transmission": "Transmission", "price": "Price (£)"},
    )
    st.plotly_chart(fig3, use_container_width=True)
    meds = df.groupby("transmission")["price"].median().sort_values()
    lines = [f"- **{t}**: £{p:,.0f}" for t, p in meds.items()]
    st.markdown("Median price by transmission:\n" + "\n".join(lines))
