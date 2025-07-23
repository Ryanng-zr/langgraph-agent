from typing import TypedDict
from agent.llm import llm

class State(TypedDict):
    input: str
    decision: str
    output: str

def MON_Agent(state: State):
    print("Reached fuel node")
    prompt = (
        "Aircraft A has 100L fuel. Aircraft B has 10000L fuel. Aircraft C has 0L fuel.\n"
        f"User input: {state['input']}\n"
        "Recommend the aircraft with the most fuel. Respond only like: 'Aircraft B: 10000L'"
    )
    return {"output": llm().generate_content(prompt).text}
