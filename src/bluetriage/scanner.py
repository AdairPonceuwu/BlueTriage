from __future__ import annotations
import json
from pathlib import Path
from .normalize import normalize_windows_json
from .models import NormalizedEvent, Alert
from .rules.builtin_rules import run_all_rules


def load_events_json(path: Path) -> list[NormalizedEvent]:
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, list):
        raise ValueError("Input JSON must be a list of events")
    return [normalize_windows_json(e) for e in data]


def scan(path: Path) -> list[Alert]:
    events = load_events_json(path)
    return run_all_rules(events)
