Artifacts Example

This folder contains example artifacts copied from MLflow `mlruns` to serve as submission evidence for Kriteria 2.

Files included:

- `MLmodel` : MLflow model metadata.
- `model.pkl` : trained model (pickle binary).
- `conda.yaml` : conda environment used to create the model.
- `requirements.txt` : pip requirements for the model environment.
- `estimator.html` : estimator report (HTML) produced by the training code (e.g., scikit-learn inspection report).

How to load the model

Using MLflow (recommended if MLflow is available):

```python
import mlflow
model_path = "Membangun_model/artifacts_example"
# load by run-relative or local path to the model folder
pyfunc_model = mlflow.pyfunc.load_model(model_path)
pred = pyfunc_model.predict(pd.DataFrame({"Year":[2026]}))
```

Using pickle (if you prefer):

```python
import pickle
with open('Membangun_model/artifacts_example/model.pkl','rb') as f:
    model = pickle.load(f)
# example prediction
print(model.predict([[2026]]))
```

Notes:
- The `model.pkl` here is the same binary as the original run; ensure compatibility of Python and library versions when loading.
- To reproduce the exact environment, create a conda env from `conda.yaml` or install from `requirements.txt`.
