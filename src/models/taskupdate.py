from pydantic import BaseModel
from src.models.statusmanager import StatusManager


class TaskUpdate(BaseModel):
    #Classe focada na rota de Updates
    task: str | None = None
    status: StatusManager | None = None