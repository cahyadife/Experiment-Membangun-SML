# Membangun_model

Folder ini berisi tahapan pembuatan model machine learning untuk Kriteria 2.

## Struktur

- `modelling.py` : training model menggunakan MLflow autolog
- `modelling_tuning.py` : training model dengan hyperparameter tuning dan manual logging
- `namadataset_preprocessing/` : dataset siap dipakai
- `screenshoot_artifak.jpg` : screenshot artefak MLflow
- `screenshoot_dashboard.jpg` : screenshot dashboard/logging
- `requirements.txt` : dependencies untuk menjalankan training lokal
- `DagsHub.txt` : tautan DagsHub jika diperlukan untuk Advanced

## Artifacts (dihasilkan oleh `mlflow.autolog()`)

Contoh struktur artefak yang dihasilkan oleh `mlflow.autolog()` pada folder `mlruns`:

- `mlruns/<experiment_id>/<run_id>/artifacts/estimator.html` — laporan estimator (HTML)
- `mlruns/<experiment_id>/models/<model_version>/artifacts/MLmodel` — metadata model
- `mlruns/<experiment_id>/models/<model_version>/artifacts/model.pkl` — binary model (pickle)
- `mlruns/<experiment_id>/models/<model_version>/artifacts/conda.yaml` — environment conda
- `mlruns/<experiment_id>/models/<model_version>/artifacts/python_env.yaml` — environment details
- `mlruns/<experiment_id>/models/<model_version>/artifacts/requirements.txt` — pip requirements

Di folder ini sudah tersedia contoh artefak hasil training:

- `mlruns/1/f0c5df018cfa4504a9fd4da37a1fa17e/artifacts/estimator.html`
- `mlruns/1/models/m-8fdf8f8531774850aa0b02bc95e03cb3/artifacts/model.pkl`
- `mlruns/1/models/m-8fdf8f8531774850aa0b02bc95e03cb3/artifacts/MLmodel`
- `mlruns/1/models/m-8fdf8f8531774850aa0b02bc95e03cb3/artifacts/conda.yaml`

Jika ingin, saya bisa menambahkan tangkapan layar (dashboard) atau menyalin artefak contoh ke folder `artifacts_example/` untuk bukti tambahan.
