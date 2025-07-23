from agent.config import GEMINI_API_KEY
import google.generativeai as genai

print("Gemini API Key:", GEMINI_API_KEY)
genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel("gemini-2.0-flash")

def llm():
    return model