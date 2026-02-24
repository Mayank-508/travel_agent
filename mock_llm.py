import os
import traceback
from google.adk.models.base_llm import BaseLlm
from google.adk.models.registry import LLMRegistry
from google.adk.models.llm_request import LlmRequest
from google.adk.models.llm_response import LlmResponse
from google.genai import types

def generate_mock_response(agent_type: str, prompt: str) -> str:
    agent_type = agent_type.lower()
    if "transport" in agent_type:
        return (
            "### Transport Options\n"
            "1. Flight (GoAir 101) - $150\n"
            "2. Express Train - $50\n"
            "Recommendation: Flight is currently the best option."
        )
    elif "stay" in agent_type:
        return (
            "### Stay Recommendations\n"
            "1. Seaside Resort - $120/night\n"
            "2. City Center Hotel - $90/night\n"
            "Recommendation: Seaside Resort matches the requirement."
        )
    elif "itinerary" in agent_type:
        return (
            "### Day-wise Plan\n"
            "**Day 1:** Arrive, Check-in to accommodation. Gentle evening walk.\n"
            "**Day 2:** Local sightseeing and main attractions.\n"
            "**Day 3:** Shopping for souvenirs, depart.\n\n"
            "Estimated trip cost is well within your stated budget."
        )
    return "Default Mock response"

class ResilientLLM(BaseLlm):
    """
    A unified LLM wrapper that attempts to use the real Gemini model first.
    If it fails due to Quota/Rate Limits, Missing Keys, or Network issues, it seamlessly
    switches to a local rule-based MockLLM to keep the system running.
    """
    model: str = "gemini-2.5-pro"
    agent_type: str = "general"

    async def generate_content_async(
        self, llm_request: LlmRequest, stream: bool = False
    ):
        use_fallback = os.getenv("USE_FALLBACK_MODE", "false").lower() == "true"
        
        if not use_fallback:
            try:
                # Attempt to yield from the actual model
                real_llm = LLMRegistry.new_llm(self.model)
                async for chunk in real_llm.generate_content_async(llm_request, stream=stream):
                    yield chunk
                return
            except Exception as e:
                print(f"\n[Warning] Gemini API call failed: {e}. Auto-switching to rule-based fallback mode for {self.agent_type}.\n")
                use_fallback = True

        if use_fallback:
            # Fallback mock logic
            prompt = ""
            if llm_request.contents:
                for content in llm_request.contents:
                    if content.parts:
                        for part in content.parts:
                            if part.text:
                                prompt += part.text + " "
            
            response_text = generate_mock_response(self.agent_type, prompt)
            
            # ADK expects an AsyncGenerator of LlmResponse chunks. Return our synthetic response.
            yield LlmResponse(
                partial=False, 
                content=types.Content(role="model", parts=[types.Part(text=response_text)])
            )
