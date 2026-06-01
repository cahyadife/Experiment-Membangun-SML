FROM python:3.11-slim

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends build-essential git && rm -rf /var/lib/apt/lists/*

COPY conda.yaml .
RUN python -m pip install --upgrade pip
RUN pip install mlflow scikit-learn pandas matplotlib requests

COPY modelling.py .
COPY namadataset_preprocessing/ namadataset_preprocessing/

ENTRYPOINT ["python", "modelling.py", "--data_path", "namadataset_preprocessing/indonesia_gdp_preprocessed.csv"]
