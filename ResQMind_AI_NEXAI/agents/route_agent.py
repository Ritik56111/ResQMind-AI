def suggest_route(incident):
    return {"recommendation":"Alternate Route","reason":"Primary segment is simulated as blocked."} if incident["traffic_blocked"] else {"recommendation":"Normal Route","reason":"No simulated blockage detected."}
