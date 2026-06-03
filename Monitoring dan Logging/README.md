# Monitoring dan Logging

Folder ini berisi konfigurasi dasar untuk serving model, Prometheus monitoring, Grafana dashboard, dan alerting.

## Isi folder

- `1.bukti_serving.png` : bukti serving model MLflow pada port 5700
- `2.prometheus.yml` : konfigurasi Prometheus
- `3.prometheus_exporter.py` : exporter Python untuk expose metriks model
- `4.bukti monitoring Prometheus/` : bukti monitoring Prometheus
- `5.bukti monitoring Grafana/` : bukti monitoring Grafana
- `6.bukti alerting Grafana/` : bukti alerting Grafana
- `7.inference.py` : script inferensi model dari artefak MLflow
- `Dockerfile` : image container untuk exporter dan inferensi
- `docker-compose.yml` : stack Prometheus + Grafana + exporter
- `requirements.txt` : dependensi Python
- `grafana/` : provisioning Grafana dashboard "dashboard-cahyadi"

## Prometheus metrics yang diekspos

Metrik utama yang diekspos oleh exporter:

- `ml_model_requests_total`
- `ml_model_request_errors_total`
- `ml_model_request_latency_seconds_bucket`
- `ml_model_active_requests`
- `ml_model_prediction_value`
- `ml_model_input_year`
- `ml_model_prediction_sum`
- `ml_model_prediction_count`
- `ml_model_prediction_average`
- `ml_model_prediction_min`
- `ml_model_prediction_max`

Prometheus dapat memuat metrik ini di `http://localhost:5800`.

## Cara menjalankan

1. Buka folder `Monitoring dan Logging`
2. Jalankan:

```bash
python -m pip install -r requirements.txt
python 3.prometheus_exporter.py
```

3. Buka Prometheus di `http://localhost:5800`
4. Buka Grafana di `http://localhost:5890` (admin/admin)

## Docker Compose

```bash
docker compose up --build
```

Grafana akan otomatis memuat dashboard `dashboard-cahyadi`.

Pastikan screenshot Grafana menampilkan nama dashboard `dashboard-cahyadi` yang berisi username Dicoding.

Bukti Prometheus dan Grafana bisa ditaruh di folder:

- `4.bukti monitoring Prometheus/`
- `5.bukti monitoring Grafana/`
- `6.bukti alerting Grafana/`
- `Monitoring dan Logging/1.bukti_serving.png`

Panduan bukti tambahan tersedia di `prometheus_grafana_evidence.md`.

## Alerting

Prometheus rule file sudah disiapkan di `alert_rules.yml`.

Aturan alert yang tersedia:
- `HighRequestLatency`
- `ModelErrorRate`
- `HighActiveRequests`

Untuk menampilkan alert di Grafana, buka menu Alerting lalu gunakan dashboard `dashboard-cahyadi`.
