def recommend_resources(incident, risk):
    ambulances=3 if incident["injured"]>=5 else 2 if incident["injured"]>=2 else 1
    return {"ambulances":ambulances,"traffic_control":incident["traffic_blocked"],"fire_unit":"smoke/fire risk" in incident["hazards"]}
