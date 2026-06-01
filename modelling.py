import pandas as pd
import mlflow
import mlflow.sklearn
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# 1. Load data
df = pd.read_csv('indonesia_gdp_preprocessed.csv')

# 2. Persiapan Fitur (Gunakan Tahun untuk prediksi PDB)
X = df[['Year']]
y = df['GDP_USD']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 3. MLflow Tracking
mlflow.set_experiment("Analisa_Ekonomi_Indonesia")
mlflow.sklearn.autolog() # Mengaktifkan autologging

with mlflow.start_run(run_name="LinearRegression_Baseline"):
    model = LinearRegression()
    model.fit(X_train, y_train)
    
    # Evaluasi sederhana
    predictions = model.predict(X_test)
    mse = mean_squared_error(y_test, predictions)
    r2 = r2_score(y_test, predictions)
    
    print(f"Model Trained. MSE: {mse}, R2: {r2}")
