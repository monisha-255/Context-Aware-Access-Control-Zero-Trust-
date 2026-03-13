# Access Policies

This document defines the policy rules used by the Context-Aware Access Control system.

## Policy Rules

The access decision is determined by the total risk score calculated from contextual signals.

| Risk Score | Decision | Description |
| :--- | :--- | :--- |
| **0 – 2** | `ALLOW` | Full access granted to the requested resource. |
| **3 – 5** | `MFA REQUIRED` | Access granted only after high-assurance authentication. |
| **6 – 7** | `LIMITED ACCESS` | Access granted with restricted permissions (e.g., read-only, no downloads). |
| **8+** | `DENY` | Access blocked due to critical risk level. |

## Context Scoring Model

The Risk Scoring Engine uses the following weights to calculate the total score:

| Signal | Condition | Weight |
| :--- | :--- | :--- |
| **Device** | Personal Device | +2 |
| **Network** | Public WiFi | +3 |
| **Location** | Foreign Country | +4 |
| **Application** | Finance / Sensitive App | +3 |
| **Other** | Corporate Device / Office Network | 0 |
