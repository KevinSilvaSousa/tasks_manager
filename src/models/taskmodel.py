from pydantic import BaseModel, Field
from datetime import datetime
from src.models.statusmanager import StatusManager

class TaskModel(BaseModel):
    # MODELO DA TASK 

    id: int
    task: str
    status: StatusManager
    creation_date: datetime = Field(default_factory = datetime.now)