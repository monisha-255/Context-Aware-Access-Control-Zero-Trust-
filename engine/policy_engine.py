def access_decision(risk_score):
    """
    Determines the access decision based on the risk score.
    """
    if risk_score <= 2:
        return "ALLOW"
    elif risk_score <= 5:
        return "MFA REQUIRED"
    elif risk_score <= 7:
        return "LIMITED ACCESS"
    else:
        return "DENY"
