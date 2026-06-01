# Submission Update Log

This file records the steps taken to reorganize and finalize the submission structure for Cahyadi.

## Actions performed

- Reorganized repository into the required submission structure:
  - `Eksperimen_SML_Cahyadi/` for preprocessing (Kriteria 1)
  - `Membangun_model/` for model training and MLflow artifacts (Kriteria 2)
  - `Workflow-CI/` for MLflow Project and CI workflow files (Kriteria 3)
  - `Monitoring dan Logging/` for monitoring and logging artifacts (Kriteria 4)

- Created preprocessing files in `Eksperimen_SML_Cahyadi/preprocessing/`:
  - `Eksperimen_Cahyadi.ipynb`
  - `automate_Cahyadi.py`
  - preprocessed dataset copied to `namadataset_preprocessing/`

- Moved model files into `Membangun_model/` and preserved required artifacts:
  - `modelling.py`
  - `modelling_tuning.py`
  - `requirements.txt`
  - `DagsHub.txt`
  - `screenshoot_dashboard.jpg`
  - `screenshoot_artifak.jpg`
  - MLflow outputs and related artifacts

- Moved CI workflow into `Workflow-CI/`:
  - `.github/workflows/mlflow-ci.yml`
  - `.workflow/`
  - `MLProject/` including `MLproject`, `conda.yaml`, and `modelling.py`
  - `docker_hub_link.txt`

- Ensured `Monitoring dan Logging/` contains a placeholder `1.bukti_serving` and the file `7.Inference.py`.

- Created the final submission archive `SMSML_Cahyadi.zip` containing only:
  - `Eksperimen_SML_Cahyadi.txt`
  - `Membangun_model/`
  - `Workflow-CI.txt`
  - `Monitoring dan Logging/`

- Committed and pushed the reorganized structure to `origin master` on GitHub.

## Changes Made in Second Round (Review Fixes)

- Updated `Eksperimen_SML_Cahyadi.txt` with proper repository URL and description (Kriteria 1).
- Updated `Workflow-CI.txt` with proper repository URL, Docker Hub link, and branch info (Kriteria 3).
- Updated `Monitoring dan Logging/1.bukti_serving` with MLflow serving command examples and status.

## Remaining Tasks

- **Kriteria 2 Screenshots**: Validate that `screenshoot_artifak.jpg` and `screenshoot_dashboard.jpg` properly show MLflow autolog artifacts and UI.
- **Kriteria 4 Serving Evidence**: Add actual screenshot evidence showing `http://127.0.0.1:5000` or Docker output.
- **Kriteria 4 Prometheus Evidence**: Ensure screenshots show all three metrics properly exposed.
- **Kriteria 4 Grafana Dashboard**: Verify dashboard name is `dashboard-cahyadi_ca` in monitoring screenshots.
- **Kriteria 4 Alerting**: Ensure alerting evidence folder contains both rules and notification screenshots.

## Notes for next agent

- Review `instructions.md` first to understand what has already been done.
- Validate the final archive `SMSML_Cahyadi.zip` and ensure no nested zip files exist.
- If needed, update the root README or the submission archive to match reviewer format exactly.

