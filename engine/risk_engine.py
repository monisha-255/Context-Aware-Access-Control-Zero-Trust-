def calculate_risk(context):
    """
    Calculates a comprehensive risk score based on identity, device posture,
    location, and application risk profile.
    """
    risk = 0

    # 1. Device Posture Signals
    posture = context.get("device_posture", {})
    if not posture.get("managed", False):
        risk += 3  # High risk if not a corporate-managed device
    if not posture.get("antivirus_active", True):
        risk += 4  # Critical security failure
    if not posture.get("disk_encryption", True):
        risk += 3
    if posture.get("os_patch_level") == "outdated":
        risk += 2

    # 2. Location & Network Signals
    if context.get("location") == "foreign":
        risk += 4
    
    network = context.get("network_type", "public")
    if network == "public_wifi":
        risk += 3
    elif network == "home":
        risk += 1
    elif network == "corporate":
        risk += 0

    # 3. Application Risk Profile
    app_risk = context.get("application_risk", "low")
    if app_risk == "critical":
        risk += 5
    elif app_risk == "high":
        risk += 3
    
    # 4. Identity Context
    if context.get("user_role") == "guest":
        risk += 2
    
    return risk
