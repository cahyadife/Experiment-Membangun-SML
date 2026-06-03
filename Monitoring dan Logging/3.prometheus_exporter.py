import argparse
import json
import time
from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path
from urllib.parse import parse_qs, urlparse

import mlflow.pyfunc
import pandas as pd
from prometheus_client import Gauge, Histogram, Counter, start_http_server


SCRIPT_DIR = Path(__file__).resolve().parent
DEFAULT_MODEL_PATH = SCRIPT_DIR / 'mlruns' / '1' / 'models' / 'm-8fdf8f8531774850aa0b02bc95e03cb3' / 'artifacts'

REQUEST_COUNTER = Counter('ml_model_requests_total', 'Total model requests', ['endpoint'])
REQUEST_ERRORS = Counter('ml_model_request_errors_total', 'Total failed model requests', ['endpoint'])
REQUEST_LATENCY = Histogram('ml_model_request_latency_seconds', 'Latency of model requests', ['endpoint'])
ACTIVE_REQUESTS = Gauge('ml_model_active_requests', 'Active model request count')
LAST_PREDICTION = Gauge('ml_model_prediction_value', 'Last model prediction value')
INPUT_YEAR = Gauge('ml_model_input_year', 'Last input year value')
PREDICTION_SUM = Gauge('ml_model_prediction_sum', 'Cumulative sum of predicted GDP values')
PREDICTION_COUNT = Gauge('ml_model_prediction_count', 'Number of predictions made')
PREDICTION_AVERAGE = Gauge('ml_model_prediction_average', 'Average prediction value')
PREDICTION_MIN = Gauge('ml_model_prediction_min', 'Minimum prediction value seen')
PREDICTION_MAX = Gauge('ml_model_prediction_max', 'Maximum prediction value seen')


class PredictionHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        parsed = urlparse(self.path)
        if parsed.path != '/predict':
            self.send_error(404, 'Not Found')
            return

        start = time.time()
        endpoint = '/predict'
        ACTIVE_REQUESTS.inc()
        REQUEST_COUNTER.labels(endpoint=endpoint).inc()

        try:
            params = parse_qs(parsed.query)
            year_values = params.get('year')
            if not year_values:
                raise ValueError('Parameter "year" diperlukan sebagai query string.')

            year = int(year_values[0])
            prediction_input = pd.DataFrame({'Year': [year]})
            prediction = float(self.server.model.predict(prediction_input)[0])

            LAST_PREDICTION.set(prediction)
            INPUT_YEAR.set(year)
            self.server.total_predictions += 1
            self.server.prediction_sum += prediction
            self.server.prediction_average = self.server.prediction_sum / self.server.total_predictions
            self.server.prediction_min = min(self.server.prediction_min, prediction)
            self.server.prediction_max = max(self.server.prediction_max, prediction)

            PREDICTION_SUM.set(self.server.prediction_sum)
            PREDICTION_COUNT.set(self.server.total_predictions)
            PREDICTION_AVERAGE.set(self.server.prediction_average)
            PREDICTION_MIN.set(self.server.prediction_min)
            PREDICTION_MAX.set(self.server.prediction_max)

            response = {
                'year': year,
                'prediction': float(prediction),
                'count': self.server.total_predictions,
            }
            payload = json.dumps(response).encode('utf-8')
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.send_header('Content-Length', str(len(payload)))
            self.end_headers()
            self.wfile.write(payload)
        except Exception as e:
            REQUEST_ERRORS.labels(endpoint=endpoint).inc()
            self.send_error(400, str(e))
        finally:
            duration = time.time() - start
            REQUEST_LATENCY.labels(endpoint=endpoint).observe(duration)
            ACTIVE_REQUESTS.dec()

    def log_message(self, format, *args):
        return


class MetricsHTTPServer(HTTPServer):
    def __init__(self, server_address, RequestHandlerClass, model):
        super().__init__(server_address, RequestHandlerClass)
        self.model = model
        self.total_predictions = 0
        self.prediction_sum = 0.0
        self.prediction_average = 0.0
        self.prediction_min = float('inf')
        self.prediction_max = float('-inf')


def parse_args():
    parser = argparse.ArgumentParser(description='Prometheus exporter untuk model MLflow.')
    parser.add_argument('--model-path', type=str, default=str(DEFAULT_MODEL_PATH))
    parser.add_argument('--port', type=int, default=5880)
    parser.add_argument('--predict-port', type=int, default=5881)
    return parser.parse_args()

def main():
    args = parse_args()

    model_path = Path(args.model_path).resolve()

    if not model_path.exists():
        raise FileNotFoundError(f'Model path tidak ditemukan: {model_path}')

    model = mlflow.pyfunc.load_model(str(model_path))
    start_http_server(args.port)

    print(f'Starting metrics service on port {args.port}')
    print(f'Starting prediction service on port {args.predict_port}')
    server = MetricsHTTPServer(('', args.predict_port), PredictionHandler, model)
    server.serve_forever()


if __name__ == '__main__':
    main()
