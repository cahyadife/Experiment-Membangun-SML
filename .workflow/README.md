# Workflow CI

Folder ini berisi dokumentasi dan dukungan untuk workflow CI yang dibuat untuk project MLflow.

Struktur yang disiapkan:
- `MLProject/` : folder MLflow Project utama
- `.github/workflows/mlflow-ci.yml` : workflow GitHub Actions untuk retraining, artefak, dan build Docker image

Gunakan secrets GitHub berikut di repository:
- `DOCKERHUB_USERNAME`
- `DOCKERHUB_TOKEN`

Workflow ini menggunakan `mlflow run` untuk melatih model, mengupload artefak ke GitHub Actions artifacts, dan `mlflow build-docker` untuk membuat image Docker.
