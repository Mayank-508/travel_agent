from google.adk.agents import Agent
from google.adk.tools.google_search_tool import GoogleSearchTool

from mock_llm import ResilientLLM

# 1. Transport Research Agent
transport_agent = Agent(
    name="transport_research_agent",
    model=ResilientLLM(model="gemini-2.5-pro", agent_type="transport"),
    tools=[GoogleSearchTool()], # Built-in ADK tool
    instruction=(
        "You are an expert travel coordinator. Search for current transport options to the specified destination. "
        "Prioritize safety, cost-effectiveness, and direct routes. "
        "Your goal: Identify the best, most cost-effective, and convenient transport options (flights, trains, etc.) to the user's destination."
    )
)
