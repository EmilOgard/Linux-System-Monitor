import psutil
from datetime import datetime, timezone

def collect_metrics():
    return {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "cpu": psutil.cpu_percent(interval=1),
        "memory": psutil.virtual_memory().percent,
        "disk": psutil.disk_usage("/").percent,
        "process_count": len(psutil.pids())
    }