from risk_engine import calculate_risk
from policy_engine import access_decision

def evaluate_access(context):
    """
    Evaluates contextual signals and returns a final access decision.
    """
    risk = calculate_risk(context)
    decision = access_decision(risk)

    return {
        "risk_score": risk,
        "decision": decision,
        "context": context
    }
