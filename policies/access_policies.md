# Access Policies (Zero Trust)

This document defines the advanced context-aware policy rules.

## Context Scoring Matrix

The risk score is a sum of signals across four dimensions:

### 1. Device Posture
| Signal | Weight | Action on High Score |
| :--- | :--- | :--- |
| Unmanaged Device | +3 | Limit Access |
| Antivirus Disabled | +4 | Block / Remediation |
| No Disk Encryption | +3 | Limit Access |
| Outdated OS Patch | +2 | Remediation Prompt |

### 2. Location & Network
| Signal | Weight |
| :--- | :--- |
| Foreign Country | +4 |
| Public WiFi | +3 |
| Home Network | +1 |
| Corporate/Whitelisted | 0 |

### 3. Application Risk
| Signal | Weight |
| :--- | :--- |
| Critical (M&A, HR, Finance) | +5 |
| High (CRM, Internal Tools) | +3 |
| Low (Wiki, Public Site) | 0 |

## Dynamic Access Decisions

| Total Risk Score | Decision Action | Security Response |
| :--- | :--- | :--- |
| **0 – 2** | `ALLOW` | Full access granted. |
| **3 – 5** | `MFA REQUIRED` | Require Step-up Auth. |
| **3 – 5 (WiFi + High Risk App)** | `BROWSER ISOLATION` | Render in secure container. |
| **6 – 7** | `LIMITED ACCESS` | Read-only; No Download/Print. |
| **6 – 7 (Posture Issue)** | `REMEDIATION` | Captive portal for updates. |
| **8+** | `DENY` | Access Blocked; **Alert Security Team**. |
