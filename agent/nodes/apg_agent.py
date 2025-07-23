from typing import TypedDict
from agent.llm import llm

class State(TypedDict):
    input: str
    decision: str
    output: str

def APG_Agent(state: State):
    print("Reached munition node")
    prompt = (
        "Aircraft A has 10000 munition. Aircraft B has 1000 munition. Aircraft C has 0 munition.\n"
        f"User input: {state['input']}\n"
        "Recommend the aircraft with the most munition. Respond only like: 'Aircraft A: 10000'"
    )
    return {"output": llm().generate_content(prompt).text}
