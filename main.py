import os 
from fastapi import FastAPI, Depends
from pydantic import BaseModel
from src.ai.gemini import Gemini # can also do .ai.gemini (tells python src is root folder)
from src.auth.throttling import apply_rate_limiter
from src.auth.dependencies import get_user_identifier


def load_system_prompt():
    with open('src/system_prompt.md', 'r') as f: # current file open and being run is fastAPIGemini
        return f.read()

system_prompt = load_system_prompt()
gemini_api_key = 'AIzaSyAOmDycQQLX1REEY74PRnUwigPBfEbGuho' # os.getenv('GEMINI_API_KEY')

ai_platform = Gemini(api_key=gemini_api_key, system_prompt=system_prompt)

# initialise
app = FastAPI()

class ChatRequest(BaseModel):
    prompt: str

class ChatResponse(BaseModel):  
    response: str


@app.get('/')
async def root():
    return {'message': 'API is running'}

@app.post('/chat', response_model=ChatResponse)
async def chat(request: ChatRequest, user_id: str = Depends(get_user_identifier)):
    apply_rate_limiter(user_id) # called every request
    response_text = ai_platform.chat(request.prompt)
    return ChatResponse(response=response_text)


