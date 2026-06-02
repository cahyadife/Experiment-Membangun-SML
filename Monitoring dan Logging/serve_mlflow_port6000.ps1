# Serve MLflow model on port 6000
# Usage: Open an environment where mlflow is installed, then run this script in PowerShell:
#   powershell -ExecutionPolicy Bypass -File .\serve_mlflow_port6000.ps1

# Path to local model folder containing MLmodel (adjust if needed)
$MODEL_PATH = "Membangun_model/artifacts_example"

# Start MLflow model server on port 6000 without creating a conda env
mlflow models serve -m "$MODEL_PATH" -p 6000 --no-conda

# Expected log output includes a line like:
# INFO:waitress:Serving on http://127.0.0.1:6000
# Capture a screenshot of that terminal showing the full address.
