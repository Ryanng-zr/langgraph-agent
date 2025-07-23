from typing import TypedDict

from agent.llm import llm

class State(TypedDict):
    input: str
    decision: str
    output: str

def llm_call_router(state: State):
    print("Reached router")
    prompt = (
        "You are a router. Classify this input as 'munition', 'fuel', or 'range'. If the user asks for remote assistance, classify as 'remote' and add all user input after this.\n"
        "Only return one word, and in remote context, include the user input after 'remote'.\n"
        f"User: {state['input']}"
    )
    decision = llm().generate_content(prompt).text.strip().lower()
    return {"decision": decision}
