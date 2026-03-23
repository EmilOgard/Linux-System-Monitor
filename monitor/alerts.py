import subprocess
import logging

logging.basicConfig(
    filename="alerts.log",
    level=logging.WARNING,
    format="%(asctime)s - %(message)s"
)

def send_notification(message):
    """Send notification to desktop"""
    try:
        subprocess.run(["notify-send", "System Alert", message])
    except Exception:
        pass

def check_alerts(metrics, config):
    alerts = []

    if metrics["cpu"] > config.get("cpu_threshold", 80):
        alerts.append(f"High CPU usage: {metrics['cpu']}%")

    if metrics["memory"] > config.get("memory_threshold", 80):
        alerts.append(f"High memory usage: {metrics['memory']}%")

    if metrics["disk"] > config.get("disk_threshold", 80):
        alerts.append(f"High disk usage: {metrics['disk']}%")

    return alerts

def handle_alerts(alerts):
    """Process alerts"""
    for alert in alerts:
        logging.warning(alert)
        send_notification(alert)