# Eksperimen SML Cahyadi

[![GitHub Actions](https://github.com/cahyadica/Eksperimen_SML_Cahyadi/actions/workflows/mlflow-ci.yml/badge.svg)](https://github.com/cahyadica/Eksperimen_SML_Cahyadi/actions/workflows/mlflow-ci.yml)
[![Docker Pulls](https://img.shields.io/docker/pulls/cahyadica/eksperimen_sml?logo=docker)](https://hub.docker.com/r/cahyadica/eksperimen_sml)
[![Docker Build](https://img.shields.io/docker/cloud/build/cahyadica/eksperimen_sml?logo=docker)](https://hub.docker.com/r/cahyadica/eksperimen_sml)

Repository ini berisi eksperimen machine learning untuk prediksi GDP Indonesia menggunakan MLflow Project dan GitHub Actions CI.

## Struktur

- `MLProject/` : MLflow Project untuk retraining model
  - `modelling.py` : skrip training dan logging model
  - `conda.yaml` : environment MLflow Project
  - `MLproject` : definisi entry point MLflow
  - `Dockerfile` : Docker build container untuk training
  - `README.md` : dokumentasi MLflow Project
  - `namadataset_preprocessing/` : dataset preprocessing
- `.github/workflows/mlflow-ci.yml` : GitHub Actions workflow CI
- `.workflow/README.md` : dokumentasi workflow

## Cara menggunakan

### Jalankan lokal dengan MLflow Project

```bash
cd MLProject
mlflow run .
```

### Bangun Docker image lokal

```bash
cd MLProject
docker build -t cahyadica/eksperimen_sml:latest .
```

### Jalankan container Docker

```bash
docker run --rm cahyadica/eksperimen_sml:latest
```

## GitHub Actions CI

Workflow CI sudah disiapkan pada `.github/workflows/mlflow-ci.yml`. Workflow ini akan:

1. Melatih model lewat `mlflow run`.
2. Mengupload artefak `mlruns` sebagai GitHub Actions artifact.
3. Membangun Docker image menggunakan `mlflow build-docker`.
4. Mendorong image ke Docker Hub.

### Secrets yang diperlukan

- `DOCKERHUB_USERNAME`
- `DOCKERHUB_TOKEN`

## Docker Hub

Image Docker yang dibangun oleh workflow akan menggunakan tag:

`<DOCKERHUB_USERNAME>/eksperimen_sml:latest`

## Monitoring dan Logging

Folder `Monitoring dan Logging/` berisi konfigurasi Prometheus, Grafana, exporter Python, dan proof-of-concept dashboard `cahyadi_ca`.

- `Monitoring dan Logging/2.prometheus.yml`
- `Monitoring dan Logging/3.prometheus_exporter.py`
- `Monitoring dan Logging/7.inference.py`
- `Monitoring dan Logging/docker-compose.yml`
- `Monitoring dan Logging/grafana/` provisioning Grafana
