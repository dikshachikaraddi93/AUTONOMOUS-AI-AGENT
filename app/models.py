from pydantic import BaseModel
from typing import List


class AgentRequest(BaseModel):
    request: str


class AgentResponse(BaseModel):
    status: str
    tasks: List[str]
    document: str
    response: str