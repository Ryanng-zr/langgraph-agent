from langgraph.graph import StateGraph, START, END
from typing import TypedDict

from agent.router import llm_call_router
from agent.nodes.apg_agent import APG_Agent
from agent.nodes.mon_agent import MON_Agent
from agent.nodes.mps_agent import MPS_Agent
from agent.remote_nodes.remote_node import call_remote_graph

# --- State definition ---
class State(TypedDict):
    input: str
    decision: str
    output: str

# --- Router logic ---
def route_decision(state: State):
    match state["decision"]:
        case "munition":
            return "APG_Agent"
        case "fuel":
            return "MON_Agent"
        case "range":
            return "MPS_Agent"
        case "remote":
            return "call_remote_graph"
        # case _:
        #     raise ValueError(f"Unknown decision: {state['decision']}")

# --- Graph construction ---
def build_langgraph():
    """
    Build the LangGraph workflow for the agent.
    """
    graph = StateGraph(State)

    graph.set_entry_point("llm_call_router")

    graph.add_node("llm_call_router", llm_call_router)
    graph.add_node("APG_Agent", APG_Agent)
    graph.add_node("MON_Agent", MON_Agent)
    graph.add_node("MPS_Agent", MPS_Agent)
    graph.add_node("call_remote_graph", call_remote_graph)

    graph.add_conditional_edges("llm_call_router", route_decision, {
        "APG_Agent": "APG_Agent",
        "MON_Agent": "MON_Agent",
        "MPS_Agent": "MPS_Agent",
        "call_remote_graph": "call_remote_graph"
    })

    graph.add_edge("APG_Agent", END)
    graph.add_edge("MON_Agent", END)
    graph.add_edge("MPS_Agent", END)
    graph.add_edge("call_remote_graph", END)

    workflow = graph.compile()
    return workflow
