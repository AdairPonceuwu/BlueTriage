from __future__ import annotations
from typing import Any, Optional
from pydantic import BaseModel, Field
from typing import List


class NormalizedEvent(BaseModel):
    timestamp: str
    event_id: int
    host: str = "unknown"
    user: Optional[str] = None
    source_ip: Optional[str] = None
    message: Optional[str] = None
    raw: dict[str, Any] = Field(default_factory=dict)


class Alert(BaseModel):
    rule_id: str
    title: str
    severity: str  # low/medium/high
    reason: str
    mitre: Optional[str] = None
    next_steps: List[str] = Field(default_factory=list)
    tags: List[str] = Field(default_factory=list)
    event: NormalizedEvent
