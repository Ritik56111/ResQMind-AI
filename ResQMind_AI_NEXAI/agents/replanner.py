def replan(plan,update):
    p=dict(plan)
    p["actions"]=["Escalate fire-risk monitoring and request additional hazard containment support.","Keep casualty response as the first priority.","Treat the primary traffic segment as fully blocked and maintain alternate routing.","Re-check resource availability before any real-world dispatch decision."]
    p["priority"]="Injured First → Fire/Hazard Containment → Alternate Routing"
    p["rationale"]=plan["rationale"]+" New update detected: "+update["new_hazard"]+"."
    return p
