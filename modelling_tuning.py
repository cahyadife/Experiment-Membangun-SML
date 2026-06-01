import pandas as pd
import numpy as np
import mlflow
import mlflow.sklearn
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error

# 1. Load data
df = pd.read_csv('indonesia_gdp_preprocessed.csv')
X = df[['Year']]
y = df['GDP_USD']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 2. MLflow Setup
mlflow.set_experiment("Analisa_Ekonomi_Indonesia_Tuning")

# 3. Hyperparameter Tuning dengan Manual Logging
with mlflow.start_run(run_name="RF_Hyperparameter_Tuning"):
    rf = RandomForestRegressor(random_state=42)
    param_grid = {
        'n_estimators': [50, 100],
        'max_depth': [None, 10, 20]
    }
    
    grid_search = GridSearchCV(estimator=rf, param_grid=param_grid, cv=3, scoring='r2')
    grid_search.fit(X_train, y_train)
    
    best_model = grid_search.best_estimator_
    predictions = best_model.predict(X_test)
    
    # Manual Logging Params & Metrics
    mlflow.log_params(grid_search.best_params_)
    mlflow.log_metric("mse", mean_squared_error(y_test, predictions))
    mlflow.log_metric("r2_score", r2_score(y_test, predictions))
    
    # Artifact: Residual Plot
    plt.figure(figsize=(10,6))
    plt.scatter(y_test, predictions)
    plt.xlabel('Actual')
    plt.ylabel('Predicted')
    plt.title('Actual vs Predicted GDP')
    plt.savefig("actual_vs_pred.png")
    mlflow.log_artifact("actual_vs_pred.png")
    
    mlflow.sklearn.log_model(best_model, "model_rf_tuned")
    print(f"Tuning Selesai. R2 Score: {r2_score(y_test, predictions)}")
