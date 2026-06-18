from app_pages.multipage import MultiPage
from app_pages.page_summary import page_summary_body
from app_pages.page_correlation_study import page_correlation_study_body
from app_pages.page_hypotheses import page_hypotheses_body
from app_pages.page_price_predictor import page_price_predictor_body
from app_pages.page_ml_performance import page_ml_performance_body

app = MultiPage(app_name="Used Car Price Predictor")

app.add_page("Project Summary", page_summary_body)
app.add_page("Price Correlation Study", page_correlation_study_body)
app.add_page("Project Hypotheses", page_hypotheses_body)
app.add_page("Predict Sale Price", page_price_predictor_body)
app.add_page("ML Model Performance", page_ml_performance_body)

app.run()
