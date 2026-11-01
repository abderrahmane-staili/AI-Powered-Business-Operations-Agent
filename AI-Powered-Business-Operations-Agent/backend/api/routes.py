from fastapi import APIRouter, Header, HTTPException
from pydantic import BaseModel
from agents.orchestrator import dispatch, AGENTS
from services import db
from utils.config import API_KEY

router = APIRouter()

def check_key(x_api_key: str | None):
    if not API_KEY or x_api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API key")

class TaskIn(BaseModel):
    source: str
    agent: str
    payload: dict = {}

@router.get("/health")
def health():
    return {"status": "ok", "agents": list(AGENTS)}

@router.post("/tasks")
async def create_task(body: TaskIn, x_api_key: str | None = Header(default=None)):
    check_key(x_api_key)
    task = db.create_task(body.source, body.agent, body.payload)
    outcome = await dispatch(task)
    return {"task_id": task["id"], **outcome}

@router.get("/tasks/{task_id}")
def get_task(task_id: int, x_api_key: str | None = Header(default=None)):
    check_key(x_api_key)
    task = db.get_task(task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task
