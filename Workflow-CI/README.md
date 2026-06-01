# Workflow-CI

Folder ini berisi struktur untuk Kriteria 3: workflow CI menggunakan MLflow Project.

## Struktur

- `.workflow/` : dokumentasi workflow CI
- `.github/workflows/mlflow-ci.yml` : GitHub Actions workflow untuk retraining dan build Docker
- `MLProject/` : MLflow Project dengan `modelling.py`, `conda.yaml`, dan `MLproject`
- `namadataset_preprocessing/` : dataset yang digunakan oleh workflow
- `docker_hub_link.txt` : tautan Docker Hub image
- `Workflow-CI.txt` : catatan tambahan untuk workflow CI
