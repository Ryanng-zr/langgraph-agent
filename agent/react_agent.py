# agent/react_agent.py

from langchain.agents import Tool, AgentExecutor, create_react_agent
from langchain.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI

from agent.config import GEMINI_API_KEY

# Setup Gemini LLM
llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",  # or gemini-1.5-pro if needed
    google_api_key=GEMINI_API_KEY,
)# Example tools
tools = [
    Tool.from_function(
        name="search",
        description="Useful for searching current events or definitions",
        func=lambda q: f"(fake search result for: {q})",
    ),
    Tool.from_function(
        name="calculator",
        description="Useful for arithmetic",
        func=lambda q: str(eval(q)),
    ),
]

# ReAct Prompt
REACT_PROMPT = PromptTemplate.from_template("""
You are an AI agent that must always use tools to answer questions. Never answer directly. Your job is to think, select the appropriate tool, and execute it.

You have access to the following tools:

{tools}

Use the following strict format:

Question: the input question you must answer  
Thought: think carefully about which tool to use  
Action: the action to take, must be one of [{tool_names}]  
Action Input: the input to the action (plain string or number)  
Observation: the result of the action  
... (repeat Thought/Action/Observation as needed)  
Thought: I now know the final answer  
Final Answer: the final answer to the original question

IMPORTANT:
- Do NOT skip tool usage.
- Do NOT answer directly unless you’ve used at least one tool.
- Do NOT return generic answers like “I can’t do that.”

Begin!

Question: {input}
{agent_scratchpad}
""")

# Create ReAct agent + executor
agent = create_react_agent(llm, tools, REACT_PROMPT)
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)
