import argparse

import mlflow
import mlflow.sklearn
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split


def train(data_path: str, test_size: float, random_state: int, experiment_name: str) -> None:
    df = pd.read_csv(data_path)
    X = df[['Year']]
    y = df['GDP_USD']

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=random_state
    )

    mlflow.set_experiment(experiment_name)
    mlflow.sklearn.autolog()

    with mlflow.start_run(run_name='LinearRegression_Baseline'):
        model = LinearRegression()
        model.fit(X_train, y_train)

        predictions = model.predict(X_test)
        mse = mean_squared_error(y_test, predictions)
        r2 = r2_score(y_test, predictions)

        mlflow.log_metric('mse', mse)
        mlflow.log_metric('r2', r2)
        mlflow.log_param('test_size', test_size)
        mlflow.log_param('random_state', random_state)

        mlflow.sklearn.log_model(model, 'model')

        print(f'Model trained successfully.')
        print(f'MSE: {mse:.4f}')
        print(f'R2: {r2:.4f}')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Train a GDP regression model using MLflow.')
    parser.add_argument('--data_path', type=str, default='namadataset_preprocessing/indonesia_gdp_preprocessed.csv')
    parser.add_argument('--test_size', type=float, default=0.2)
    parser.add_argument('--random_state', type=int, default=42)
    parser.add_argument('--experiment_name', type=str, default='Analisa_Ekonomi_Indonesia')
    args = parser.parse_args()

    train(
        data_path=args.data_path,
        test_size=args.test_size,
        random_state=args.random_state,
        experiment_name=args.experiment_name,
    )
