from agno.agent import Agent
from agno.models.ollama import Ollama

travel_agent = Agent(
    model=Ollama(id="qwen2.5:0.5b"),
    description="Fast travel assistant",
)
