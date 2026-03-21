import time
from monitor.collector import collect_metrics

def live_stats(interval=1):
    print("Statistics (Ctrl+C to exit)\n")

    try:
        while True:
            metrics = collect_metrics()

            print(
                f"CPU USAGE: {metrics['cpu']}% | "
                f"RAM USAGE: {metrics['memory']}% | "
                f"DISK USAGE: {metrics['disk']}% | "
                f"PROCESSES: {metrics['process_count']} | "
            )

            time.sleep(interval)
        
    except KeyboardInterrupt:
        print("\nExiting\n")
