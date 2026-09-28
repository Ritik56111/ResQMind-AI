def build_plan(incident,risk,resources,route):
    actions=[f"Dispatch {resources['ambulances']} ambulance(s) for casualty support."]
    if resources["fire_unit"]: actions.append("Request fire-response unit for smoke/fire hazard containment.")
    if resources["traffic_control"]: actions.append("Deploy traffic-control support to isolate the blocked segment.")
    actions += [f"Use {route['recommendation'].lower()} for responder movement.","Prioritize injured-person assistance before secondary containment."]
    return {"priority":"Injured First → Hazard Containment → Traffic Stabilization","actions":actions,"rationale":f"Risk is {risk['level']} based on casualty load, hazards, route conditions and visibility."}
