from __future__ import annotations
from pathlib import Path
from jinja2 import Environment, FileSystemLoader, select_autoescape
from ..models import Alert

SEV_ORDER = {"high": 0, "medium": 1, "low": 2}


def render_html(alerts: list[Alert], out_path: Path) -> None:
    # Sort alerts by severity (high -> low)
    alerts_sorted = sorted(
        alerts,
        key=lambda a: SEV_ORDER.get((a.severity or "low").strip().lower(), 99),
    )

    templates_dir = Path(__file__).parent / "templates"
    env = Environment(
        loader=FileSystemLoader(str(templates_dir)),
        autoescape=select_autoescape(["html", "xml"]),
    )
    tpl = env.get_template("report.html.j2")
    html = tpl.render(
        total_alerts=len(alerts_sorted),
        alerts=[a.model_dump() for a in alerts_sorted],
    )
    out_path.write_text(html, encoding="utf-8")
