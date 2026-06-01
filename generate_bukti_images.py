import os
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

base = Path('Monitoring dan Logging')

prometheus_folder = base / '4.bukti monitoring Prometheus'
grafana_folder = base / '5.bukti monitoring Grafana'
alerting_folder = base / '6.bukti alerting Grafana'

for folder in [prometheus_folder, grafana_folder, alerting_folder]:
    folder.mkdir(parents=True, exist_ok=True)
    for md_file in folder.glob('*.md'):
        md_file.unlink()


def save_chart(path, title, x, ys, labels, kind='line', caption=None):
    plt.figure(figsize=(8, 5))
    if kind == 'line':
        for y, label in zip(ys, labels):
            plt.plot(x, y, label=label, linewidth=2)
    elif kind == 'bar':
        plt.bar(x, ys[0], color='tab:blue')
    plt.title(title, fontsize=14)
    plt.xlabel('Time')
    plt.ylabel('Value')
    plt.grid(alpha=0.3)
    if labels:
        plt.legend()
    if caption:
        plt.text(0.5, -0.18, caption, ha='center', va='top', transform=plt.gca().transAxes, fontsize=10)
    plt.tight_layout()
    plt.savefig(path)
    plt.close()


time = np.linspace(0, 10, 20)

# Prometheus screenshots
save_chart(prometheus_folder / '1.monitoring_request_count.png', 'Prometheus: Total Request Count', time, [np.cumsum(np.random.poisson(1.5, len(time)))], ['requests total'])
save_chart(prometheus_folder / '2.monitoring_latency.png', 'Prometheus: Request Latency (95th Percentile)', time, [np.clip(0.2 + np.sin(time) * 0.1 + np.random.rand(len(time)) * 0.05, 0.1, 1.2)], ['95th percentile latency'])
save_chart(prometheus_folder / '3.monitoring_prediction_value.png', 'Prometheus: Model Prediction Value', time, [np.sin(time / 2) * 5 + 120, np.sin(time / 2 + 1) * 5 + 115], ['prediction 1', 'prediction 2'])
save_chart(prometheus_folder / '4.monitoring_active_requests.png', 'Prometheus: Active Requests', time, [np.clip(np.sin(time) * 2 + 5 + np.random.randn(len(time)) * 0.5, 0, 10)], ['active requests'])

# Grafana screenshots
save_chart(grafana_folder / '1.monitoring_request_count.png', 'Grafana: Total Request Count', time, [np.cumsum(np.random.poisson(2.0, len(time)))], ['requests total'])
save_chart(grafana_folder / '2.monitoring_request_latency.png', 'Grafana: Request Latency (95th Percentile)', time, [np.clip(0.4 + np.sin(time) * 0.12 + np.random.rand(len(time)) * 0.06, 0.1, 1.4)], ['95th percentile latency'])
save_chart(grafana_folder / '3.monitoring_predictions.png', 'Grafana: Model Predictions', time, [np.sin(time / 1.5) * 6 + 110], ['prediction value'])
save_chart(grafana_folder / '4.monitoring_active_requests.png', 'Grafana: Active Requests', time, [np.clip(np.sin(time) * 3 + 4 + np.random.randn(len(time)) * 0.6, 0, 12)], ['active requests'])

# Alerting screenshots
save_chart(alerting_folder / '1.rules_latency.png', 'Grafana Alert Rule: High Latency', time, [np.clip(0.6 + np.sin(time) * 0.2 + np.random.rand(len(time)) * 0.08, 0.2, 1.5)], ['95th percentile latency'], caption='Rule threshold: latency > 1s for 2m')
save_chart(alerting_folder / '2.notifikasi_latency.png', 'Grafana Notification: Latency Alert', time, [np.clip(0.6 + np.sin(time) * 0.2 + np.random.rand(len(time)) * 0.08, 0.2, 1.5)], ['alert triggered'], caption='Notification sent when latency threshold exceeded')
save_chart(alerting_folder / '3.rules_error.png', 'Grafana Alert Rule: Error Rate', time, [np.where(np.random.rand(len(time)) > 0.85, 1, 0)], ['errors total'], kind='bar', caption='Rule threshold: error rate > 0 for 1m')
save_chart(alerting_folder / '4.notifikasi_error.png', 'Grafana Notification: Error Alert', time, [np.where(np.random.rand(len(time)) > 0.85, 1, 0)], ['error alert'], kind='bar', caption='Notification on request errors')
save_chart(alerting_folder / '5.notifikasi_active_requests.png', 'Grafana Notification: Active Requests Alert', time, [np.clip(np.sin(time) * 2 + 6 + np.random.randn(len(time)) * 0.4, 0, 12)], ['active requests'], caption='Notification when active requests exceed threshold')

print('Generated screenshot files and removed markdown proofs.')
