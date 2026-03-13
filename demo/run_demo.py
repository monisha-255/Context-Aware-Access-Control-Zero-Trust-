import sys
import os

# Add the engine directory to the path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'engine')))

from decision_engine import evaluate_access

def run_scenario(name, context):
    print(f"=== {name} ===")
    result = evaluate_access(context)
    print(f"User: {context.get('user_id')} | App: {context.get('application')}")
    print(f"Risk Score: {result['risk_score']}")
    print(f"Action: {result['action']}")
    if result['restrictions']:
        print(f"Restrictions: {', '.join(result['restrictions'])}")
    if result['alert_sent']:
        print("ALERT: Security Team Notified!")
    if result['message'] != "N/A":
        print(f"System Message: {result['message']}")
    print("-" * 40 + "\n")

if __name__ == "__main__":
    # Scenario 1: Finance Dept Access to ERP
    run_scenario("Scenario 1: Finance ERP Access", {
        "user_id": "senior_accountant",
        "user_role": "finance",
        "device_posture": {"managed": True, "antivirus_active": True, "disk_encryption": True, "os_patch_level": "current"},
        "location": "remote",
        "network_type": "corporate", # Connected via ZPA whitelisted
        "application": "ERP System",
        "application_risk": "high"
    })

    # Scenario 2: Contractor Access to Project Repo
    run_scenario("Scenario 2: Contractor Git Access", {
        "user_id": "ext_consultant",
        "user_role": "guest",
        "device_posture": {"managed": False, "antivirus_active": True, "disk_encryption": True, "os_patch_level": "current"},
        "location": "local",
        "network_type": "home",
        "application": "Git Repository",
        "application_risk": "low"
    })

    # Scenario 3: Executive Access to Sensitive Docs
    run_scenario("Scenario 3: Executive Foreign Access", {
        "user_id": "vp_finance",
        "user_role": "executive",
        "device_posture": {"managed": True, "antivirus_active": True, "disk_encryption": True, "os_patch_level": "current"},
        "location": "foreign",
        "network_type": "public",
        "application": "SharePoint M&A folder",
        "application_risk": "critical"
    })

    # Scenario 4: IT Support Access
    run_scenario("Scenario 4: IT Support Tools", {
        "user_id": "it_tech_01",
        "user_role": "it_support",
        "device_posture": {"managed": True, "antivirus_active": True, "disk_encryption": True, "os_patch_level": "current"},
        "location": "home",
        "network_type": "home",
        "application": "ServiceNow / RDP Jump Host",
        "application_risk": "low"
    })

    # Scenario 5: High-Risk App from Low-Trust Location
    run_scenario("Scenario 5: Marketing Salesforce (Public WiFi)", {
        "user_id": "marketing_coord",
        "user_role": "marketing",
        "device_posture": {"managed": True, "antivirus_active": True, "disk_encryption": True, "os_patch_level": "current"},
        "location": "local",
        "network_type": "public_wifi",
        "application": "Salesforce CRM",
        "application_risk": "high"
    })
