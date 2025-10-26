from src.ai.base import AIPlatform
import google.generativeai as genai

class Gemini(AIPlatform):
    def __init__(self, api_key: str, system_prompt: str= None):
        self.api_key = api_key
        self.system_prompt = system_prompt
        genai.configure(api_key = self.api_key) # https://ai.google.dev/gemini-api/docs/models
        self.model = genai.GenerativeModel('gemini-2.5-flash-preview-09-2025')

    def chat(self, prompt: str) -> str:
        if self.system_prompt:
            prompt = f'{self.system_prompt}\n\n{prompt}'
        response = self.model.generate_content(prompt)
        return response.text

def load_system_prompt():
    with open('src\system_prompt.md', 'r') as f:
        return f.read()