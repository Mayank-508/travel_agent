# Google ADK Multi-Agent Travel Itinerary Planner

This repository contains the scaffold for a robust Multi-Agent system built using the **Google Agent Development Kit (ADK)**. 

The architecture demonstrates a **Sequential Orchestration Pattern** where:
1. **Transport Research Agent** looks up flights/travel.
2. **Stay Recommendation Agent** builds on that to find matching hotels.
3. **Itinerary Planner Agent** synthesizes the final day-by-day plan.
The entire flow is managed continuously by a **SequentialAgent** (Root Agent).

## Project Structure

This project follows ADK conventions for modularity:
```text
travel_agent/
│
├── agent.py                 <-- Entry point exporting `root_agent`
├── sub_agents/
│   ├── transport_agent.py
│   ├── stay_agent.py
│   └── itinerary_agent.py
│
├── tools/
│   ├── preference_tools.py
│   ├── cost_tools.py
│   └── report_tools.py
│
├── problem_statement.md
├── requirements.txt
└── .env                     <-- Contains your GOOGLE_API_KEY
```

## Setup Instructions

### 1. Create and Activate a Virtual Environment
```powershell
python -m venv venv
.\venv\Scripts\activate
```

### 2. Install Dependencies
```powershell
# Installs google-adk, pydantic, requests, and dotenv
pip install -r requirements.txt
```

### 3. Set API Key
Open `.env` (make sure it is at `travel_agent/.env`) and replace `your_google_api_key_here` with your actual Gemini API Key:
```text
GOOGLE_API_KEY="AIzaSy..."
```
## Key Features

- Built using Google Agent Development Kit (ADK)
- Demonstrates Sequential Multi-Agent Orchestration
- Uses the built-in GoogleSearchTool from ADK to fetch real-world travel information
- Includes deterministic fallback responses when Gemini is unavailable
## Execution Modes & Fallback

This project supports **Two Execution Modes**:
1. **Real Execution Mode (Default)**: Leverages `gemini-2.5-pro` and built-in ADK Google Search tools.
2. **Fallback Execution Mode**: Handled automatically by the custom `ResilientLLM` wrapper. If the Gemini API hits a quota limit (429 Error) OR if you explicitly trigger it, the agents fall back to local rule-based deterministic mock responses.

To force offline Mock execution, run the CLI with the environment flag:
```powershell
$env:USE_FALLBACK_MODE="true"
adk run travel_agent
```

## Running the Application

To interactively run your multi-agent travel planner, navigate to the **parent folder** containing `travel_agent` and execute:

```powershell
adk run travel_agent
```
You can also run the web interface locally using:
```powershell
adk web travel_agent
```

Follow the prompt to provide your destination and constraints, and enjoy your automatically planned itinerary!
