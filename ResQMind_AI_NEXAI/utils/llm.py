import os, requests
def generate_explanation(plan):
    try:
        r=requests.post("http://localhost:11434/api/generate",json={"model":os.getenv("RESQMIND_OLLAMA_MODEL","llama3.2:3b"),"prompt":"Explain this emergency response plan briefly for a hackathon demo: "+str(plan),"stream":False},timeout=20)
        if r.ok: return r.json().get("response","AI explanation unavailable.")
    except Exception: pass
    return "The Coordination Agent prioritizes casualty support, hazard containment and route management. This is an illustrative simulation and should be reviewed by authorized responders."
