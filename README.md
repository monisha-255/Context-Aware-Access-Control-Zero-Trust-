# Context-Aware Access Control (Zero Trust)

This project demonstrates a dynamic, risk-based access control system built on Zero Trust principles: **"Never Trust, Always Verify."**

## Overview

Traditional security models focus on perimeter defense. Zero Trust assumes that threats exist both inside and outside the network. This system evaluates every access request by collecting contextual signals and calculating a risk score to determine the appropriate access level.

## Security Concepts

This system implements **Identity-Aware Proxy (IAP)** and **least-privilege** principles:
- **Micro-segmentation**: Connections are established directly to applications, not the network.
- **Continuous Verification**: Risk is assessed on every request, not just at login.
- **Adaptive Response**: Security controls scale based on real-time risk.

## Use Case Scenarios

The system is tested against the following real-world scenarios:
1. **Finance Dept Access to ERP**: Full access from corporate device on trusted network.
2. **Contractor Access to Git**: Restricted access for guest users on personal devices.
3. **Executive Foreign Access**: Read-only access and security alerts for sensitive data in foreign locations.
4. **IT Support Tools**: Whitelisted home access for authorized technicians.
5. **High-Risk App from Low-Trust Site**: Browser isolation for Salesforce access from public WiFi.

## Folder Structure

```
context-aware-access-control/
│
├ README.md
├ architecture/
│   └ architecture-diagram.md
│
├ policies/
│   └ access_policies.md
│
├ engine/
│   ├ context_collector.py
│   ├ risk_engine.py
│   ├ policy_engine.py
│   └ decision_engine.py
│
├ demo/
│   ├ demo_script.md
│   └ run_demo.py
│
└ requirements.txt
```
