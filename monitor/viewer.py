from pathlib import Path
from rich import print
import json

LOG_FILE = Path("metrics.log")

def show_logs(lines=10):
    if not LOG_FILE.exists():
        print("No logs found.")
        return
    
    with open(LOG_FILE, "r") as f:
        data = f.readlines()[-lines:]

    for line in data:
        entry = json.loads(line)
        print(entry)