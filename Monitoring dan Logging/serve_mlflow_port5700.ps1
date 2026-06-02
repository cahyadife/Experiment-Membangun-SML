# Serve MLflow model on port 5700
# Usage: Open an environment where mlflow is installed, then run this script in PowerShell:
#   powershell -ExecutionPolicy Bypass -File .\serve_mlflow_port5700.ps1

# Path to local model folder containing MLmodel (adjust if needed)
$MODEL_PATH = "Membangun_model/artifacts_example"

# Start MLflow model server on port 5700 without creating a conda env
$scriptPath = 'C:\Users\cahya\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0\LocalCache\local-packages\Python312\Scripts'
$env:PATH = "$scriptPath;$env:PATH"

C:\Users\cahya\AppData\Local\Microsoft\WindowsApps\python3.12.exe -m mlflow models serve -m "$MODEL_PATH" -p 5700 --no-conda
