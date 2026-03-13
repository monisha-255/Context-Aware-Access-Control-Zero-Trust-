def collect_context(user_id, device_info, location, network, application):
    """
    Simulates a context collector that aggregates signals for an access request.
    """
    # In a real system, this would query various telemetry sources.
    return {
        "user_id": user_id,
        "device": device_info,
        "location": location,
        "network": network,
        "application": application
    }
