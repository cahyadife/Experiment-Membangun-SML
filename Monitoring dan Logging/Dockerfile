FROM python:3.11-slim

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends build-essential && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN python -m pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

COPY 3.prometheus_exporter.py .

ENTRYPOINT ["python", "3.prometheus_exporter.py", "--model-path", "../mlruns/1/models/m-8fdf8f8531774850aa0b02bc95e03cb3/artifacts", "--port", "8000", "--predict-port", "5000"]
