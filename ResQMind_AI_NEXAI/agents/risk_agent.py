def assess_risk(incident):
    score=0
    if incident["injured"]>=5: score+=2
    if incident["traffic_blocked"]: score+=1
    if "smoke/fire risk" in incident["hazards"]: score+=2
    if incident["visibility"]!="Normal": score+=1
    level="CRITICAL" if score>=5 else "HIGH" if score>=3 else "MEDIUM"
    return {"level":level,"score":score,"factors":incident["hazards"] + (["casualty load"] if incident["injured"]>=5 else [])}
