from langgraph.graph import StateGraph, START, END
from typing import TypedDict

import nest_asyncio
from fastapi import FastAPI, Request
import uvicorn
import threading
from pyngrok import ngrok
import time
import json
from fastapi.responses import StreamingResponse

from agent.remote_nodes.remote_router import llm_call_remote_router
from agent.remote_nodes.remote_time import Time_Agent
from agent.remote_nodes.remote_weather import Weather_Agent
from pyngrok import ngrok

ngrok.kill()


ngrok.set_auth_token("2ytuknUzhxd3a7btNDGTGpaPCkE_2qYaEZiCHMAg2Xfco5vLy")

# --- State definition ---
class State(TypedDict):
    input: str
    decision: str
    output: str

# --- Router logic ---
def route_decision(state: State):
    match state["decision"]:
        case "weather":
            return "Weather_Agent"
        case "time":
            return "Time_Agent"

app = FastAPI()
@app.get("/")
async def read_root(request: Request):
    body = await request.json()
    return {"message": body}

nest_asyncio.apply()

import threading

def run():
    uvicorn.run(app, host='0.0.0.0', port=8000)

def run_server():
    thread = threading.Thread(target=run, daemon=True)
    thread.start()
    ngrok.kill()
    tunnel = ngrok.connect(8000, bind_tls=True)
    public_url = tunnel.public_url
    print("Public URL:", public_url)
    return public_url

run_server()

# --- Graph construction ---
def build_remote_langgraph():
    """
    Build the LangGraph workflow for the agent.
    """
    graph = StateGraph(State)

    graph.set_entry_point("llm_call_router")

    graph.add_node("llm_call_router", llm_call_remote_router)
    graph.add_node("Time_Agent", Time_Agent)
    graph.add_node("Weather_Agent", Weather_Agent)

    graph.add_conditional_edges("llm_call_router", route_decision, {
        "Time_Agent": "Time_Agent",
        "Weather_Agent": "Weather_Agent"
    })

    graph.add_edge("Time_Agent", END)
    graph.add_edge("Weather_Agent", END)

    workflow = graph.compile()

    @app.post("/invoke")
    async def invoke(request: Request):
        body = await request.json()
        result = workflow.invoke(body)
        print(result.get('output'))
        return result.get('output')
    
    @app.post("/runs/stream")
    async def run_stream(body: dict):
        def event_generator():
            for chunk in workflow.stream(body):
                payload = json.dumps(chunk)
                print("Sending Chunk:", payload)
                yield f"data: {payload}\n\n"
                time.sleep(0.01)
        return StreamingResponse(event_generator(), media_type="text/event-stream")
    return workflow, invoke, run_stream




