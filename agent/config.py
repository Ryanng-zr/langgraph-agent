# agent/config.py

import os
from dotenv import load_dotenv

# Load variables from a .env file, if present
load_dotenv()

# API Keys and Secrets
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# LangGraph-specific config
GRAPH_DEBUG = os.getenv("GRAPH_DEBUG", "false").lower() == "true"

# Other Constants
DEFAULT_SYSTEM_PROMPT = "You are a helpful LangGraph agent."
MAX_TOKENS = int(os.getenv("MAX_TOKENS", "2048"))
