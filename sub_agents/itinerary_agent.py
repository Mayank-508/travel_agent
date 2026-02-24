from google.adk.agents import Agent
from tools.cost_tools import estimate_trip_cost
from tools.report_tools import generate_itinerary_report

from mock_llm import ResilientLLM

# 3. Itinerary Planner Agent
itinerary_agent = Agent(
    name="itinerary_planner_agent",
    model=ResilientLLM(model="gemini-2.5-pro", agent_type="itinerary"),
    tools=[estimate_trip_cost, generate_itinerary_report], # Custom tools
    instruction=(
        "You are a master itinerary planner. Take travel options and hotel recommendations and organize them into "
        "a logical, geographical day-wise plan. Ensure you do not exceed the user's overall budget. "
        "Use the estimate_trip_cost tool to verify budget constraints. "
        "Finally, format your output using the generate_itinerary_report system. "
        "Your goal: Create a structured day-by-day travel plan including transport, stay, and daily activities based on prior agents' research."
    )
)
