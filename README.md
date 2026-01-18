🏠 Bangalore House Price Prediction
Description

End-to-end Machine Learning project to predict Bangalore house prices.

.Built a regression model from scratch using Python, Pandas, NumPy, and Scikit-learn.

.Performed data cleaning, feature engineering, dimensionality reduction, model selection, and cross-validation.

.Exposed the trained model through a Flask API and a minimal browser-based UI for interactive prediction.

.Deployed on Render for public access.



📌 Project Overview

This project converts raw real-estate data into a production-ready prediction system.

Includes:

✔ Data cleaning
✔ Feature engineering
✔ Dimensionality reduction
✔ Model selection & cross validation
✔ Model export (pickle)
✔ Flask REST API
✔ UI in browser
✔ Deployment on Render




🧱 System Architecture

               ┌─────────────────┐
               │   Raw Dataset   │
               └────────┬────────┘
                        ↓
               ┌─────────────────┐
               │ Data Cleaning   │
               └────────┬────────┘
                        ↓
               ┌─────────────────┐
               │ Feature Engg.   │
               └────────┬────────┘
                        ↓
               ┌─────────────────┐
               │ Model Training  │
               └────────┬────────┘
                        ↓
               ┌───────────────────────┐
               │ Pickle + Columns.json │
               └────────┬──────────────┘
                        ↓
               ┌─────────────────┐
               │ Flask API       │
               └────────┬────────┘
                        ↓
               ┌─────────────────┐
               │ Browser UI      │
               └─────────────────┘



📂 Project Structure

.
├── data/                      # raw dataset
├── model/                     # model.pkl + columns.json
├── server/                    # Flask backend
├── client/                    # UI frontend
├── requirements.txt
├── Procfile
└── README.md




🧩 Project Workflow (End-to-End)

The complete development pipeline of this project follows a real-world machine learning lifecycle:

1. Data Acquisition

.Dataset loaded from Kaggle / CSV

.Initial inspection of column types & data distribution

2. Exploratory Data Analysis (EDA)

.Performed to understand relationships & detect patterns:

.Distribution plots (histograms, countplots)

.Correlation heatmap

.Outlier visualization

.Null value analysis

3. Data Cleaning

.Core cleaning tasks included:

.Handling missing values (mean/median/most-freq strategies)

.Removing outliers using IQR / domain logic

.Removing duplicates

.Feature normalization & scaling

4. Feature Engineering

.New features were created to improve model accuracy:

.Domain-based derived features

.Encoding categorical variables

.Normalization for numerical variables

.Train-test splitting for supervised learning

5. Dimensionality Reduction

.To reduce feature complexity and improve training efficiency:

.PCA (Principal Component Analysis) applied

.Components selected based on explained variance threshold

.Reduced computational cost without losing key information

6. Model Selection

.Multiple algorithms were benchmarked:

.Linear Regression

.Decision Tree

.Lasso Regression

7. Model Evaluation & Cross-Validation

.Used proper evaluation techniques:

.K-Fold Cross Validation

.Classification metrics (Accuracy, Precision, Recall, F1, AUC)

.Comparisons tabulated to identify best performer

8. Final Model Training

.The best model was retrained on full training set:

.Hyperparameter tuning performed (GridSearch / RandomizedSearch)

.Final performance validated on unseen test data

.Linear Regression was chosen for providing high accuracy.

9. Model Serialization

.Once finalized, model was exported for deployment using: pickle

10. Backend (Flask Web App)

🌐 Flask API Endpoints

| Endpoint              | Method | Description                    |
| --------------------- | ------ | ------------------------------ |
| `/get_location_names` | GET    | Returns list of location names |
| `/predict_home_price` | POST   | Predicts house price           |


POST Body Example:

{
  "total_sqft": 1200,
  "bhk": 3,
  "bath": 3,
  "location": "Whitefield"
}

response:

{
  "estimated_price": 84.5
}


🎨 Frontend UI

Built using:

HTML

CSS

JavaScript

User inputs → AJAX request → shows estimated price.

🚀 Deployment Ready

Configured with:

✔ requirements.txt
✔ Procfile for Gunicorn
✔ virtual env support
✔ Flask entrypoint updated to production mode

Supports deployment on:

->Render



🧾 Tech Stack

| Category        | Tools                       |
| --------------- | --------------------------- |
| Language        | Python                      |
| ML              | Pandas, NumPy, Scikit-Learn |
| Backend         | Flask                       |
| Serving         | Gunicorn                    |
| Deployment      | Render                      |
| Version Control | Git + GitHub                |


🎯 Highlights

✔ Complete ML workflow
✔ Real-world dataset
✔ Advanced outlier removal
✔ Cross validated model
✔ API + UI for real usage
✔ Deployment ready build


📍 Conclusion

This project demonstrates converting raw data into a production-grade predictive system combining:

Data Science + ML Engineering + Software + Deployment.
