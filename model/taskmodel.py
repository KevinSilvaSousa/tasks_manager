from pydantic import BaseModel, Field
from datetime import datetime

class TaskModel(BaseModel):


    id: int
    task: str
    completed: bool = False
    creation_date: datetime = Field(default_factory = datetime.now)