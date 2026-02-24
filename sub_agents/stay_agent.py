from google.adk.agents import Agent
from google.adk.tools.google_search_tool import GoogleSearchTool

from mock_llm import ResilientLLM

# 2. Stay Recommendation Agent
stay_agent = Agent(
    name="stay_recommendation_agent",
    model=ResilientLLM(model="gemini-2.5-pro", agent_type="stay"),
    tools=[GoogleSearchTool()],
    instruction=(
        "You are a hospitality expert. Find highly-rated hotels and neighborhoods that match the user's interests. "
        "Provide estimated cost-per-night and reasoning for each location. "
        "Your goal: Recommend accommodations that fit the user's budget and proximity to travel interests."
    )
)
