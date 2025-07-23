import gradio as gr
from agent.graph import build_langgraph

# Build the graph
graph = build_langgraph()

chat_history = []

def chat(user_input):
    global chat_history

    state = {"input": user_input}

    result = graph.invoke(state)

    response = result.get("output", "(No response)")

    chat_history.append((user_input, response))

    return chat_history

with gr.Blocks() as demo:
    gr.Markdown("## 💬 LangGraph Chatbot")

    chatbot = gr.Chatbot()
    user_input = gr.Textbox(placeholder="Type your question...", lines=1)

    def on_submit(input_text):
        return chat(input_text)

    user_input.submit(on_submit, inputs=user_input, outputs=chatbot)

demo.launch()
