from fastapi import FastAPI,Request
from routers import api
from pydantic import BaseModel

app = FastAPI()

class inputQuestion(BaseModel):
    askQuestion : str
    
app.include_router(api.router)

@app.post("/conversationAI")
def index(request:Request,inputQ:inputQuestion):
    return {'result': {'name':'Welcome to Chat-GPT Conversational AI application'}}
