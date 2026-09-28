# ResQMind AI — NEXAI

Autonomous Emergency Response Intelligence

## Team
- Ritik Kaushal — Team Leader
- Nishita Kumari — Member
- Risabh Maurya — Member

## Flow
Incident → Understand → Assess → Plan → Replan

## Agents
Incident Agent • Risk Agent • Resource Agent • Route Agent • Coordination Agent • RePlanning Agent

## Run in VS Code / PowerShell
```powershell
python -m venv .venv
.venv\Scripts\activate
python -m pip install -r requirements.txt
python -m streamlit run app.py
```

Optional local GenAI with Ollama:
```powershell
ollama pull llama3.2:3b
```

The core app works without Ollama. This is a hackathon simulation using simulated incidents and illustrative what-if outputs; it is not connected to real emergency dispatch systems.
