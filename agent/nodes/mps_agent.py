from typing import TypedDict
from agent.llm import llm

class State(TypedDict):
    input: str
    decision: str
    output: str

def MPS_Agent(state: State):
    print("Reached range node")
    prompt = (
        "Aircraft A has 0 weapon range. Aircraft B has 1000 weapon range. Aircraft C has 10000 weapon range.\n"
        f"User input: {state['input']}\n"
        "Recommend the aircraft with the most weapon range. Respond only like: 'Aircraft C: 10000'"
    )
    return {"output": llm().generate_content(prompt).text}
