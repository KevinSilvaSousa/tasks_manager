from fastapi import HTTPException
from src.data.tasks import tasks

def check_tasks(id):    # Modelos de Negocio   
    for task in tasks:
        if task.id == id:
            return task
  
    raise HTTPException(status_code=404, detail="404 Not Found")


def duplicate_id(id):
    for task in tasks:
        if task.id == id:
            return True

    return False
    

        