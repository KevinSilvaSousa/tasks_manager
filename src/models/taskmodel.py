from pydantic import BaseModel, Field
from datetime import datetime
from model.statusmanager import StatusManager

class TaskModel(BaseModel):

    id: int
    task: str
    status: StatusManager
    creation_date: datetime = Field(default_factory = datetime.now)