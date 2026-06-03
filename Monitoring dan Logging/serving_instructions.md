Serving MLflow model (port 5700)

1. Prepare environment

- Activate your Python environment with `mlflow` installed (or use conda env from `Membangun_model/artifacts_example/conda.yaml`).

2. Start the model server (PowerShell)

Use the port-5700 script:

```powershell
powershell -ExecutionPolicy Bypass -File Monitoring\ dan\ Logging\serve_mlflow_port5700.ps1
```

Or run directly:

```powershell
C:\Users\cahya\AppData\Local\Microsoft\WindowsApps\python3.12.exe -m mlflow models serve -m "Membangun_model/artifacts_example" -p 5700 --no-conda
```

If port 6000 fails, use 5700 instead.

3. Verify server is running

- Expected log line: `INFO:     Uvicorn running on http://127.0.0.1:5700`
- Test a prediction (example):

```powershell
curl -X POST http://127.0.0.1:5700/invocations -H "Content-Type: application/json" -d "{\"dataframe_split\": {\"columns\": [\"Year\"], \"data\": [[2026]]}}"
```

4. Capture evidence

- Take a screenshot of the terminal showing `Uvicorn running on http://127.0.0.1:5700`.
- Optionally, take a screenshot of the successful `curl` response showing the prediction.
- Save screenshots to `Monitoring dan Logging/1.bukti_serving.png`.

Notes and troubleshooting

- If you see version mismatches warnings (sklearn/pickle), create a conda env from `conda.yaml` and run without `--no-conda`.
- Use the `MLmodel` metadata and `requirements.txt` / `conda.yaml` to reproduce the server environment.
