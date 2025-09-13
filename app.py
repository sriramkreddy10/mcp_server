from fastapi import FastAPI, Request
from pydantic import BaseModel
from typing import Union, Dict, Any
from agent.task_router import route_task

app = FastAPI(
    title="MCP Server",
    description="An async-ready Model-Compute Paradigm server",
    version="0.1.0"
)

# Define a request schema
class Task(BaseModel):
    type: str
    input: Union[str, Dict[str, Any]]

@app.post("/task")
async def handle_task(task: Task):
    result = await route_task(task.model_dump())
    return result
