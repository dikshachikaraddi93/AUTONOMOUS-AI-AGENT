from fastapi import FastAPI
from app.models import AgentRequest, AgentResponse
from app.planner import create_plan
from app.executor import execute_plan

app = FastAPI(
    title="Autonomous AI Agent",
    description="Python AI Engineer Assignment",
    version="1.0"
)


@app.get("/")
def home():
    return {
        "message": "Autonomous AI Agent is Running 🚀"
    }


@app.post("/agent", response_model=AgentResponse)
def run_agent(request: AgentRequest):

    # Step 1: Create execution plan
    tasks = create_plan(request.request)

    # Step 2: Execute plan
    result = execute_plan(request.request, tasks)

    return result