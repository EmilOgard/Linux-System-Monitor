import typer
import subprocess
import os
from monitor.runner import run_monitor
from monitor.viewer import show_logs
from monitor.stats import live_stats

app = typer.Typer(help="CLI for system monitor")

@app.command()
def start():
    """Start monitor service"""
    #run_monitor()
    subprocess.Popen(
        ["python3", "-m", "monitor.runner"],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        stdin=subprocess.DEVNULL,
        preexec_fn=os.setpgrp   
    )
    print("Monitor running in background...")

@app.command()
def stop():
    """Stop monitor service"""
    subprocess.run(["pkill", "-f", "monitor.runner"])

@app.command()
def logs(lines: int = 10):
    """Show last N log entries"""
    show_logs(lines)

@app.command()
def stats():
    """Show live system statistics"""
    live_stats()

if __name__ == "__main__":
    app()