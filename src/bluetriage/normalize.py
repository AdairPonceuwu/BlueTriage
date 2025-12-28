from __future__ import annotations
from typing import Any
from .models import NormalizedEvent


def normalize_windows_json(e: dict[str, Any]) -> NormalizedEvent:
    """
    Accepts a simple JSON event and normalizes it.
    Expected minimal fields:
      - timestamp (str)
      - event_id (int)
    Optional:
      - host, user, source_ip, message
    """
    return NormalizedEvent(
        timestamp=str(e.get("timestamp", "unknown")),
        event_id=int(e.get("event_id", -1)),
        host=str(e.get("host", "unknown")),
        user=e.get("user"),
        source_ip=e.get("source_ip"),
        message=e.get("message"),
        raw=e,
    )
