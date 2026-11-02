from src.exceptions.task_duplicated_error import DuplicateTaskError 
from src.data.tasks import tasks

# Modelos de Negocio   

def check_tasks(id):    
    for task in tasks:
        if task.id == id:
            return task
  
    raise DuplicateTaskError(status_code=404, detail="404 Not Found")


def task_id_exists(id):
    for task in tasks:
        if task.id == id:
            return True

    return False
    

        