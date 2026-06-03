from pathlib import Path

import matplotlib.pyplot as plt
import mlflow
import mlflow.sklearn
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.model_selection import GridSearchCV, train_test_split


SCRIPT_DIR = Path(__file__).resolve().parent
DATASET_PATH = SCRIPT_DIR / 'namadataset_preprocessing' / 'indonesia_gdp_preprocessed.csv'
PLOT_PATH = SCRIPT_DIR / 'actual_vs_pred.png'

# 1. Load data
df = pd.read_csv(DATASET_PATH)
X = df[['Year']]
y = df['GDP_USD']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 2. MLflow Setup & DagsHub Integration
try:
    import dagshub
    dagshub.init(repo_owner='cahyadica', repo_name='Eksperimen_SML_Cahyadi', mlflow=True)
    print("DagsHub integration initialized.")
except ImportError:
    print("DagsHub package not found, using local MLflow tracking.")
except Exception as e:
    print(f"DagsHub initialization skipped: {e}")

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
    
    # Artifact 1: Residual Plot (Actual vs Predicted)
    plt.figure(figsize=(10,6))
    plt.scatter(y_test, predictions, color='blue', alpha=0.7)
    plt.xlabel('Actual')
    plt.ylabel('Predicted')
    plt.title('Actual vs Predicted GDP')
    plt.savefig(PLOT_PATH)
    mlflow.log_artifact(PLOT_PATH)
    
    # Artifact 2: Residuals Distribution Plot
    residuals = y_test - predictions
    plt.figure(figsize=(10,6))
    plt.hist(residuals, bins=15, color='orange', edgecolor='black', alpha=0.7)
    plt.xlabel('Residuals (Actual - Predicted)')
    plt.ylabel('Frequency')
    plt.title('Distribution of Residuals')
    residuals_plot_path = SCRIPT_DIR / 'residuals.png'
    plt.savefig(residuals_plot_path)
    mlflow.log_artifact(residuals_plot_path)
    
    # Artifact 3: Metrics JSON
    import json
    metrics_data = {
        "mse": float(mean_squared_error(y_test, predictions)),
        "rmse": float(np.sqrt(mean_squared_error(y_test, predictions))),
        "mae": float(mean_absolute_error(y_test, predictions)),
        "r2_score": float(r2_score(y_test, predictions))
    }
    metrics_json_path = SCRIPT_DIR / 'metrics.json'
    with open(metrics_json_path, 'w') as f:
        json.dump(metrics_data, f, indent=4)
    mlflow.log_artifact(metrics_json_path)
    
    mlflow.sklearn.log_model(best_model, "model_rf_tuned")
    print(f"Tuning Selesai. R2 Score: {r2_score(y_test, predictions)}")
