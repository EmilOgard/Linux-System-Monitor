import time
from monitor.collector import collect_metrics
from monitor.storage import save
from monitor.alerts import check_alerts
from monitor.config import load_config

if __name__ == "__main__":
    #run_monitor()