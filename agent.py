import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

from google.adk.agents import SequentialAgent
from sub_agents.transport_agent import transport_agent
from sub_agents.stay_agent import stay_agent
from sub_agents.itinerary_agent import itinerary_agent

# Exposed root agent for ADK CLI
root_agent = SequentialAgent(
    name="travel_planner_orchestrator",
    sub_agents=[
        transport_agent,
        stay_agent,
        itinerary_agent
    ]
)

