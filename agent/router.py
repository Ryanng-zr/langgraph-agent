from typing import TypedDict

import google.generativeai as genai

genai.configure(api_key="GEMINI_API_KEY")

model = genai.GenerativeModel("gemini-2.0-flash")

class State(TypedDict):
    input: str
    decision: str
    output: str

def llm_call_router(state: State):
    print("Reached router")
    prompt = (
        "You are a router. Classify this input as 'munition', 'fuel', or 'range'. "
        "Only return one word.\n"
        f"User: {state['input']}"
    )
    decision = model.generate_content(prompt).text.strip().lower()
    return {"decision": decision}
