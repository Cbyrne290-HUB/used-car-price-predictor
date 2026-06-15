# Used Car Price Predictor

A machine-learning Data App that predicts the resale price of a used car from its
attributes, built for a used-car dealership that needs fast, consistent,
data-driven pricing of stock.

<!-- TODO: add a screenshot / link to the live Heroku app once deployed -->
**Live app:** _to be added_

---

## Table of Contents
- [Dataset Content](#dataset-content)
- [Business Requirements](#business-requirements)
- [Hypotheses and Validation](#hypotheses-and-validation)
- [Mapping Business Requirements to Visualisations and ML Tasks](#mapping-business-requirements-to-visualisations-and-ml-tasks)
- [ML Business Case](#ml-business-case)
- [Dashboard Design](#dashboard-design)
- [CRISP-DM Workflow](#crisp-dm-workflow)
- [Unfixed Bugs](#unfixed-bugs)
- [Deployment](#deployment)
- [Main Data Analysis and ML Libraries](#main-data-analysis-and-ml-libraries)
- [Credits](#credits)

---

## Dataset Content
<!-- Pass 1.1: describe the dataset contents (rows, columns, what each represents). -->
_TODO: source, licence/attribution, number of rows, and a table describing every variable._

## Business Requirements
<!-- Pass 1.1: state the business requirements clearly. -->
_TODO:_
- **Business Requirement 1:** _the client wants to understand how car attributes relate to price (data visualisation)._
- **Business Requirement 2:** _the client wants to predict the price of any used car (ML prediction)._

## Hypotheses and Validation
<!-- Merit 1.2 / Distinction: at least THREE hypotheses, each with a validation method. -->
_TODO (minimum 3):_
- **H1 –** _higher mileage lowers price._ Validation: _correlation / PPS + scatter plot._
- **H2 –** _newer cars (lower age) command higher prices._ Validation: _correlation + plot._
- **H3 –** _transmission / fuel type shifts price._ Validation: _group comparison + box plots._

## Mapping Business Requirements to Visualisations and ML Tasks
<!-- Pass 2.1: user-story format. Pass 2.2: at least one ML task named here. -->
_TODO: for each business requirement, a user story mapped to the specific
Data Visualisation tasks and the ML task(s) that satisfy it._

## ML Business Case
<!-- Pass 3.2 + Distinction: use proper ML terminology ("Machine Learning Terminology"). -->
_TODO: aim of the predictive task, learning method (supervised regression),
ideal outcome, success/failure metrics, model output and its relevance to the
user, heuristics, and the training data used._

## Dashboard Design
<!-- Pass 6.1: list each page, its content (text/plots/widgets) and which requirement it answers. -->
_TODO (bullet per page):_
- **Project Summary** – _content … answers …_
- **Price Correlation Study** – _content … answers BR1._
- **Project Hypotheses** – _content … answers …_
- **Predict Sale Price** – _content … answers BR2._
- **ML Model Performance** – _content … answers …_

## CRISP-DM Workflow
_TODO: short note mapping the notebooks to CRISP-DM stages
(Business Understanding → Data Understanding → Data Preparation → Modelling →
Evaluation → Deployment)._

## Unfixed Bugs
_TODO: list any, or state there are none known._

## Deployment
### Heroku
_TODO: deployment steps and live URL._
The app is configured for Heroku via `Procfile`, `requirements.txt`,
`runtime.txt`, and `setup.sh`.

## Main Data Analysis and ML Libraries
<!-- Distinction craftsmanship: name each library and give a usage example. -->
_TODO: pandas, numpy, scikit-learn, feature-engine, ppscore, matplotlib,
seaborn, plotly, streamlit — one usage example each._

## Credits
<!-- Plagiarism rule: attribute dataset source and any referenced code. -->
- **Dataset:** _source + link + licence._
- _Any other acknowledgements._
