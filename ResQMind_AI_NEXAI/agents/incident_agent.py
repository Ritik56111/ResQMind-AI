def analyze_incident(data):
    return {"event_type":data["type"],"location":data["location"],"injured":data["injured"],"hazards":["smoke/fire risk"] if data["smoke"] else ["water hazard"],"traffic_blocked":data["blocked"],"visibility":data["visibility"],"hospital_capacity":data["hospital_capacity"]}
