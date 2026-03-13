# Zero Trust Demo Script

This script outlines the test cases used to demonstrate the Context-Aware Access Control system.

## Test Case 1: Ideal Scenario
- **User**: Employee
- **Device**: Corporate Laptop
- **Network**: Office Network
- **Application**: Email
- **Expected Result**: Risk Score: 0, Decision: **ALLOW**

## Test Case 2: Remote Work (Medium Risk)
- **User**: Employee
- **Device**: Personal Laptop (+2)
- **Network**: Home Network (+1)
- **Application**: Internal Tool
- **Expected Result**: Risk Score: 3, Decision: **MFA REQUIRED**

## Test Case 3: Public/High Risk Scenario
- **User**: Employee
- **Device**: Unknown Device (+2)
- **Network**: Public WiFi (+3)
- **Location**: Foreign Location (+4)
- **Application**: Finance App (+3)
- **Expected Result**: Risk Score: 12, Decision: **DENY**

## Executing the Demo
Run the provided Python script to see these evaluations in action:
```bash
python run_demo.py
```
