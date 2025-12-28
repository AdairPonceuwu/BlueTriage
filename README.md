![CI](../../actions/workflows/ci.yml/badge.svg)

# BlueTriage

BlueTriage is a Windows log triage mini-engine:
- Ingest JSON events
- Normalize to a common schema
- Run detections (rule-based)
- Export alerts + generate HTML report

## Included detections (MVP)

| Rule | Windows Event ID(s) | Severity | MITRE |
|------|----------------------|----------|------|
| WIN-4625 | 4625 | Medium | T1110 |
| WIN-4720 | 4720 | High | T1136 |
| WIN-4728-4732 | 4728, 4732 | High | T1098 |
| WIN-4698 | 4698 | High | T1053.005 |

## Report preview
![Report](docs/screenshots/report.png)

## Roadmap
- [ ] Support EVTX ingestion (Windows Event Log export)
- [ ] YAML-based rules (Sigma-lite)
- [ ] Severity scoring and sorting (High → Low)
- [ ] Markdown report output (ticket-friendly)


## Quickstart (Windows / venv)

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -e .
bluetriage scan-json data\sample_events.json --out alerts.json
bluetriage report-html alerts.json --out report.html
