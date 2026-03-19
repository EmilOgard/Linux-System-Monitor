import json
from pathlib import Path

LOG_FILE = Path("metrics.log")

def save(metrics):
    with open(LOG_FILE, "a") as f:
        f.write(json.dumps(metrics) + "\n")