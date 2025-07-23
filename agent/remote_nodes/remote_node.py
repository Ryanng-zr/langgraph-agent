from langgraph.pregel.remote import RemoteGraph
from agent.remote_graph import run_server, build_remote_langgraph

graph = build_remote_langgraph()

public_url = run_server()

def call_remote_graph(state):
    remote = RemoteGraph("remote-graph", url=public_url)
    input_text = state["input"]
    result = remote.invoke({"input": input_text})
    return {"input": result}

# for chunk in remote.stream({"input": "Recommend an aircraft with the most weapon range"}):
#     print(chunk)