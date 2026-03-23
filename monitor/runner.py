import time
import logging
from monitor.collector import collect_metrics
from monitor.storage import save
from monitor.alerts import check_alerts, handle_alerts
from monitor.config import load_config

def run_monitor():
    config = load_config()

    print("Starting system monitor...")
    logging.info("System monitor started")

    while True:
        metrics = collect_metrics()
        save(metrics)

        alerts = check_alerts(metrics, config)
        handle_alerts(alerts)
        #for alert in alerts:
        #    print("[ALERT]", alert)
        
        time.sleep(config.get("interval", 5))


if __name__ == "__main__":
    run_monitor()