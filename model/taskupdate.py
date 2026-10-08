from pydantic import BaseModel
from model.statusmanager import StatusManager


class TaskUpdate(BaseModel):
    task: str | None = None
    status: StatusManager | None = None