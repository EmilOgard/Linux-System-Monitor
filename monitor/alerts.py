
def check_alerts(metrics, config):
    alerts = []

    if metrics["cpu"] > config.get("cpu_threshold", 80):
        alerts.append(f"High CPU usage: {metrics['cpu']}%")

    if metrics["memory"] > config.get("memory_threshold", 80):
        alerts.append(f"High memory usage: {metrics['memory']}%")

    if metrics["cpu"] > config.get("disk_threshold", 80):
        alerts.append(f"High disk usage: {metrics['disk']}%")

    return alerts
