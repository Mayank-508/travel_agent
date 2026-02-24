# Problem Statement: Multi-Agent Travel Itinerary Planner

## Objective
Build a Multi-Agent Travel Itinerary Planner using the Google Agent Development Kit (ADK). The system should take minimal user inputs (destination, budget, duration, and interests) and generate a comprehensive travel plan utilizing specialized AI agents.

## Requirements

1. **Architecture**
   - 1 Root Agent (Orchestrator)
   - Minimum 3 Sub-Agents with specialized responsibilities
   - Must demonstrate agent orchestration using a clear pattern (sequential, parallel, or loop).

2. **Core Agent Roles**
   - **Transport Research Agent:** Finds travel options using Google Search.
   - **Stay Recommendation Agent:** Finds hotels and best areas to stay.
   - **Itinerary Planner Agent:** Builds a logical day-wise schedule based on prior findings.

3. **Required Capabilities**
   - Integration of the built-in `GoogleSearchTool`.
   - At least 3 custom Python tools:
     - `estimate_trip_cost()`
     - `extract_user_preferences()`
     - `generate_itinerary_report()`

4. **Technical Constraints**
   - Use a stable Gemini model (e.g., `gemini-2.5-pro`).
   - Clean, modular code structure following Google ADK best practices.
   - Separate definitions for tools, agents, and orchestration.
   - Clear local development setup instructions.
