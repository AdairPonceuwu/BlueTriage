from pathlib import Path
from bluetriage.scanner import load_events_json


def test_sample_events_generate_4_alerts():
    events = load_events_json(Path("data/sample_events.json"))
    # Import here to avoid CLI deps
    from bluetriage.rules.builtin_rules import run_all_rules

    alerts = run_all_rules(events)
    assert len(alerts) >= 4


def test_failed_logon_rule_present():
    events = load_events_json(Path("data/sample_events.json"))
    from bluetriage.rules.builtin_rules import run_all_rules

    alerts = run_all_rules(events)
    ids = {a.rule_id for a in alerts}
    assert "WIN-4625" in ids
