# BlueTriage

BlueTriage is a Windows log triage mini-engine:
- Ingest JSON events
- Normalize to a common schema
- Run detections (rule-based)
- Export alerts + generate HTML report

## Quickstart (Windows / venv)

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -e .
bluetriage scan-json data\sample_events.json --out alerts.json
bluetriage report-html alerts.json --out report.html
