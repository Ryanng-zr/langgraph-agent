from typing import TypedDict
from agent.llm import llm

class State(TypedDict):
    input: str
    decision: str
    output: str

def Weather_Agent(state: State):
    prompt = (
        "You are a weather agent. Your task is to provide weather information based on user input.\n"
        f"User input: {state['input']}\n"
        "Provide the weather information in Singapore right now and respond with the result.\n Mention that you are a remote agent.\n"
    )
    return {"output": llm().generate_content(prompt).text}
