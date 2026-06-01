# Monitoring dan Logging

Folder ini berisi konfigurasi dasar untuk serving model, Prometheus monitoring, Grafana dashboard, dan alerting.

## Isi folder

- `1.bukti_serving` : placeholder bukti serving model
- `2.prometheus.yml` : konfigurasi Prometheus
- `3.prometheus_exporter.py` : exporter Python untuk expose metriks model
- `4.bukti monitoring Prometheus/` : placeholder bukti monitoring Prometheus
- `5.bukti monitoring Grafana/` : placeholder bukti monitoring Grafana
- `6.bukti alerting Grafana/` : placeholder bukti alerting Grafana
- `7.inference.py` : script inferensi model dari artefak MLflow
- `Dockerfile` : image container untuk exporter dan inferensi
- `docker-compose.yml` : stack Prometheus + Grafana + exporter
- `requirements.txt` : dependensi Python
- `grafana/` : provisioning Grafana dashboard "cahyadi_ca"

## Cara menjalankan

1. Buka folder `Monitoring dan Logging`
2. Jalankan:

```bash
python -m pip install -r requirements.txt
python 3.prometheus_exporter.py
```

3. Buka Prometheus di `http://localhost:9090`
4. Buka Grafana di `http://localhost:3000` (admin/admin)

## Docker Compose

```bash
docker compose up --build
```

Grafana akan otomatis memuat dashboard `cahyadi_ca`.

## Alerting

Prometheus rule file sudah disiapkan di `alert_rules.yml`.

Aturan alert yang tersedia:
- `HighRequestLatency`
- `ModelErrorRate`
- `HighActiveRequests`

Untuk menampilkan alert di Grafana, buka menu Alerting lalu gunakan dashboard `cahyadi_ca`.
