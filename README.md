# Context-Aware Access Control (Zero Trust)

This project demonstrates a dynamic, risk-based access control system built on Zero Trust principles: **"Never Trust, Always Verify."**

## Overview

Traditional security models focus on perimeter defense. Zero Trust assumes that threats exist both inside and outside the network. This system evaluates every access request by collecting contextual signals and calculating a risk score to determine the appropriate access level.

## Features

- **Dynamic Risk Evaluation**: Real-time assessment of signals (User, Device, Location, App).
- **Context-Aware Policy Engine**: Rules-based decision making.
- **Granular Access Levels**: From full access to outright denial.
- **Zero Trust Architecture**: Continuous verification of identity and environment.

## System Architecture

The workflow follows these steps:
`User -> Authentication -> Context Collection -> Risk Engine -> Policy Engine -> Access Decision`

See [architecture-diagram.md](./architecture/architecture-diagram.md) for more details.

## Policy Rules

- **Low Risk (0-2)**: ALLOW (Full Access)
- **Medium Risk (3-5)**: MFA REQUIRED
- **High Risk (6-7)**: LIMITED ACCESS (e.g., Read-only)
- **Critical Risk (8+)**: DENY (Access Blocked)

## How to Run the Demo

1. Ensure you have Python 3.x installed.
2. Navigate to the `demo/` directory.
3. Run the demo script:
   ```bash
   python run_demo.py
   ```

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
