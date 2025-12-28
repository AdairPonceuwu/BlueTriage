from __future__ import annotations
from pathlib import Path
import json
import typer
from .scanner import scan
from .report.render import render_html

app = typer.Typer(help="BlueTriage: normalize -> detect -> report")


@app.command()
def scan_json(input: Path = typer.Argument(..., exists=True), out: Path = Path("alerts.json")):
    """Scan a JSON file of events and write alerts to JSON."""
    alerts = scan(input)
    out.write_text(json.dumps([a.model_dump() for a in alerts], indent=2), encoding="utf-8")
    typer.echo(f"Saved {len(alerts)} alerts to {out}")


@app.command()
def report_html(
    input_alerts: Path = typer.Argument(..., exists=True),
    out: Path = Path("report.html"),
):
    """Generate an HTML report from alerts.json."""
    data = json.loads(input_alerts.read_text(encoding="utf-8"))
    from .models import Alert

    alerts = [Alert(**a) for a in data]
    render_html(alerts, out)
    typer.echo(f"Saved report to {out}")


if __name__ == "__main__":
    app()
