from pydantic import BaseModel, Field
from datetime import datetime

class TaskModel(BaseModel):
    task: str
    completed: bool = False
    creation_date: datetime = Field(default_factory = datetime.now)