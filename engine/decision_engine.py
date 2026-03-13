from risk_engine import calculate_risk
from policy_engine import get_access_decision

def evaluate_access(context):
    """
    Evaluates context to produce a detailed access decision.
    """
    risk = calculate_risk(context)
    decision_details = get_access_decision(risk, context)

    return {
        "risk_score": risk,
        "action": decision_details["action"],
        "restrictions": decision_details["restrictions"],
        "alert_sent": decision_details["alert_security"],
        "message": decision_details.get("message", "N/A")
    }
