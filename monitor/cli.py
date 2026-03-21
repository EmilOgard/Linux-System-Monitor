import typer
from monitor.runner import run_monitor
from monitor.viewer import show_logs
from monitor.stats import live_stats

app = typer.Typer(help="CLI for system monitor")

@app.command()
def start():
    """Start monitor service"""
    run_monitor()

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