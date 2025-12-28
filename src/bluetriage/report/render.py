from __future__ import annotations
from pathlib import Path
from jinja2 import Environment, FileSystemLoader, select_autoescape
from ..models import Alert


def render_html(alerts: list[Alert], out_path: Path) -> None:
    templates_dir = Path(__file__).parent / "templates"
    env = Environment(
        loader=FileSystemLoader(str(templates_dir)),
        autoescape=select_autoescape(["html", "xml"]),
    )
    tpl = env.get_template("report.html.j2")
    html = tpl.render(
        total_alerts=len(alerts),
        alerts=[a.model_dump() for a in alerts],
    )
    out_path.write_text(html, encoding="utf-8")
