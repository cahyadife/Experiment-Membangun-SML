import argparse
from pathlib import Path

import mlflow.pyfunc
import pandas as pd


def load_model(model_path: str):
    path = Path(model_path).resolve()
    if not path.exists():
        raise FileNotFoundError(f'Model path tidak ditemukan: {path}')
    return mlflow.pyfunc.load_model(str(path))


def predict_year(model, year: int):
    data = pd.DataFrame({'Year': [year]})
    prediction = model.predict(data)[0]
    return float(prediction)


def predict_batch(model, dataset_path: str):
    df = pd.read_csv(dataset_path)
    if 'Year' not in df.columns:
        raise ValueError('Dataset harus memiliki kolom Year')
    data = df[['Year']]
    predictions = model.predict(data)
    df['prediction'] = predictions
    return df


def main():
    parser = argparse.ArgumentParser(description='Inferensi model MLflow dari artefak lokal.')
    parser.add_argument('--model-path', type=str, default='../mlruns/1/models/m-8fdf8f8531774850aa0b02bc95e03cb3/artifacts')
    parser.add_argument('--year', type=int, help='Tahun yang akan diprediksi')
    parser.add_argument('--batch-path', type=str, help='Path dataset CSV untuk prediksi batch')
    parser.add_argument('--output', type=str, help='Output CSV file untuk prediksi batch')
    args = parser.parse_args()

    model = load_model(args.model_path)

    if args.year is not None:
        prediction = predict_year(model, args.year)
        print(f'Prediksi GDP untuk tahun {args.year}: {prediction:.2f}')
        return

    if args.batch_path:
        results = predict_batch(model, args.batch_path)
        if args.output:
            results.to_csv(args.output, index=False)
            print(f'Hasil prediksi disimpan di {args.output}')
        else:
            print(results.head())
        return

    parser.error('Harap berikan --year atau --batch-path untuk inferensi.')


if __name__ == '__main__':
    main()
