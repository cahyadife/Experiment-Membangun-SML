# MLProject

Project ini berisi konfigurasi MLflow Project untuk retraining otomatis model GDP Indonesia.

Folder:
- `modelling.py` : skrip training yang dapat dijalankan dari MLflow Project
- `conda.yaml` : environment MLflow Project
- `MLproject` : definisi MLflow Project
- `Dockerfile` : container image build untuk training dan inferensi
- `namadataset_preprocessing/` : folder dataset preprocessing

Docker Hub image:
- `docker.io/cahyadica/eksperimen_sml:latest`

## Menjalankan secara lokal

```bash
cd MLProject
mlflow run .
```

## Membangun Docker image lokal

```bash
cd MLProject
docker build -t cahyadica/eksperimen_sml:latest .
```

## Menjalankan Docker container

```bash
docker run --rm cahyadica/eksperimen_sml:latest
```

## Menjalankan workflow GitHub Actions

Pastikan repository memiliki secrets:
- `DOCKERHUB_USERNAME`
- `DOCKERHUB_TOKEN`

Workflow otomatis akan:
1. Melatih model menggunakan MLflow Project
2. Mengupload artefak `mlruns`
3. Membangun dan mendorong Docker image ke Docker Hub
