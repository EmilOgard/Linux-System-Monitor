import time
from monitor.collector import collect_metrics
from monitor.storage import save
from monitor.alerts import check_alerts
from monitor.config import load_config

def run_monitor():
    config = load_config()

    print("Starting system monitor...")

    while True:
        metrics = collect_metrics()
        save(metrics)

        alerts = check_alerts(metrics, config)
        for alert in alerts:
            print("[ALERT]", alert)
        
        time.sleep(config.get("interval", 5))
