def calculate_risk(context):
    """
    Calculates the total risk score based on contextual signals.
    """
    risk = 0

    # Device Posture
    if context.get("device") == "personal":
        risk += 2
    
    # Network Risk
    if context.get("network") == "public_wifi":
        risk += 3
    elif context.get("network") == "home":
        risk += 1

    # Location Risk
    if context.get("location") == "foreign":
        risk += 4

    # Application Risk
    if context.get("application") == "finance" or context.get("application") == "hr_data":
        risk += 3
    
    # User Role Risk (Optional - extending a bit)
    if context.get("user_role") == "guest":
        risk += 2

    return risk
