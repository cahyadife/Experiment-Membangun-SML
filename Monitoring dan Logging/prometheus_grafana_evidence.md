Prometheus and Grafana Evidence

Prometheus proof should show these metrics as successfully scraped and accessible in Prometheus:

- `ml_model_requests_total`
- `ml_model_request_errors_total`
- `ml_model_request_latency_seconds_bucket`
- `ml_model_active_requests`

Grafana proof should show the dashboard named `dashboard-cahyadi` and the panels connected to Prometheus metrics.

Recommended checks:

1. Open Prometheus at `http://localhost:9090`
2. Query each metric above and verify the result is non-empty.
3. Open Grafana at `http://localhost:3000`
4. Confirm dashboard name is `dashboard-cahyadi` in the browser tab and dashboard title.
5. Capture screenshots for Prometheus and Grafana:
   - `Monitoring dan Logging/4.bukti monitoring Prometheus/*`
   - `Monitoring dan Logging/5.bukti monitoring Grafana/*`
