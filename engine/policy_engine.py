def get_access_decision(risk_score, context):
    """
    Maps risk scores to advanced access decisions including isolation and alerting.
    """
    decision = {
        "action": "DENY",
        "restrictions": [],
        "alert_security": False
    }

    # High-risk scenarios always trigger alerts
    if risk_score >= 8:
        decision["alert_security"] = True

    if risk_score <= 2:
        decision["action"] = "ALLOW"
    
    elif risk_score <= 5:
        decision["action"] = "MFA REQUIRED"
        # Scenario 5: High-risk network for sensitive app
        if context.get("network_type") == "public_wifi" and context.get("application_risk") == "high":
            decision["action"] = "BROWSER ISOLATION"
            decision["restrictions"] = ["No Copy/Paste", "No Downloads"]
    
    elif risk_score <= 7:
        decision["action"] = "LIMITED ACCESS"
        decision["restrictions"] = ["Read-Only", "No Print", "No Download"]
        
        # If posture is the main issue, suggest remediation
        if not context.get("device_posture", {}).get("antivirus_active"):
            decision["action"] = "REMEDIATION REQUIRED"
            decision["message"] = "Please enable Antivirus and update patches."

    else:
        decision["action"] = "DENY"
        decision["message"] = "Access blocked due to critical risk factors."

    return decision
