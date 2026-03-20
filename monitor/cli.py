import typer
from monitor.runner import run_monitor
from monitor.viewer import show_logs

app = typer.Typer(help="CLI for system monitor")

@app.command()
def start():
    """Start monitor service"""
    run_monitor()

@app.command()
def logs(lines: int = 10):
    """Show last N log entries"""
    show_logs(lines)


if __name__ == "__main__":
    app()