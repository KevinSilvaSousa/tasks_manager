from pydantic import BaseModel
from src.models.statusmanager import StatusManager


class TaskUpdate(BaseModel):
    task: str | None = None
    status: StatusManager | None = None