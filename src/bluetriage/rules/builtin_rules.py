from __future__ import annotations
from typing import Iterable
from ..models import Alert, NormalizedEvent


def rule_failed_logons_4625(events: Iterable[NormalizedEvent]) -> list[Alert]:
    alerts: list[Alert] = []
    for ev in events:
        if ev.event_id == 4625:
            alerts.append(
                Alert(
                    rule_id="WIN-4625",
                    title="Failed logon attempt",
                    severity="medium",
                    reason="EventID 4625 indicates a failed logon; may be brute force or credential guessing.",
                    mitre="T1110",
                    tags=["authentication", "bruteforce", "windows"],
                    next_steps=[
                        "Check number of failed attempts from the same source_ip / user in a short period.",
                        "Validate whether the source_ip is expected for this host/user.",
                        "If repeated, consider blocking source and forcing password reset / MFA review.",
                    ],
                    event=ev,
                )
            )
    return alerts


def rule_user_created_4720(events: Iterable[NormalizedEvent]) -> list[Alert]:
    alerts: list[Alert] = []
    for ev in events:
        if ev.event_id == 4720:
            alerts.append(
                Alert(
                    rule_id="WIN-4720",
                    title="User account created",
                    severity="high",
                    reason="EventID 4720 indicates a new local/domain user was created. This can be legitimate or persistence.",
                    mitre="T1136",
                    tags=["account-management", "persistence", "windows"],
                    next_steps=[
                        "Confirm who created the account (correlate with related security events).",
                        "Validate with change/request or admin approval.",
                        "Review group memberships added soon after creation (4728/4732).",
                    ],
                    event=ev,
                )
            )
    return alerts


def rule_admin_group_add_4728_4732(events: Iterable[NormalizedEvent]) -> list[Alert]:
    alerts: list[Alert] = []
    for ev in events:
        if ev.event_id in (4728, 4732):
            alerts.append(
                Alert(
                    rule_id="WIN-4728-4732",
                    title="User added to privileged group",
                    severity="high",
                    reason="EventID 4728/4732 indicates a member was added to a privileged group. High risk if unexpected.",
                    mitre="T1098",
                    tags=["privilege-escalation", "account-management", "windows"],
                    next_steps=[
                        "Identify which user was added and to which group (check raw fields).",
                        "Confirm if change was approved; if not, remove membership immediately.",
                        "Investigate originating host/user and check for lateral movement signs.",
                    ],
                    event=ev,
                )
            )
    return alerts


def rule_schtask_created_4698(events: Iterable[NormalizedEvent]) -> list[Alert]:
    alerts: list[Alert] = []
    for ev in events:
        if ev.event_id == 4698:
            alerts.append(
                Alert(
                    rule_id="WIN-4698",
                    title="Scheduled task created",
                    severity="high",
                    reason="EventID 4698 indicates a scheduled task was created. Often used for persistence.",
                    mitre="T1053.005",
                    tags=["persistence", "scheduled-task", "windows"],
                    next_steps=[
                        "Review the task name, action/command, and author from event details.",
                        "Validate if the task is expected (software update, admin job, etc.).",
                        "If suspicious, disable task and investigate parent process and user activity.",
                    ],
                    event=ev,
                )
            )
    return alerts


def run_all_rules(events: list[NormalizedEvent]) -> list[Alert]:
    out: list[Alert] = []
    out.extend(rule_failed_logons_4625(events))
    out.extend(rule_user_created_4720(events))
    out.extend(rule_admin_group_add_4728_4732(events))
    out.extend(rule_schtask_created_4698(events))
    return out
