from typing import TypedDict

from agent.llm import llm

class State(TypedDict):
    input: str
    decision: str
    output: str

def llm_call_remote_router(state: State):
    print("Reached remote router")
    prompt = (
        "You are a router. Randomly classify this input as 'weather' or 'time'. "
        "Only return one word.\n"
        f"User: {state['input']}"
    )
    decision = llm().generate_content(prompt).text.strip().lower()
    return {"decision": decision}
