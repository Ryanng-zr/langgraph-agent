from typing import TypedDict
from agent.llm import llm

class State(TypedDict):
    input: str
    decision: str
    output: str

def Time_Agent(state: State):
    prompt = (
        "You are a time agent.\n"
        f"User input: {state['input']}\n"
        "Return the time in Singapore. \n Mention that you are a remote agent.\n"
    )
    return {"output": llm().generate_content(prompt).text}
