from src.exceptions.errors import DuplicateTaskError 
from src.exceptions.errors import TaskNotFoundError 
from src.data.tasks import tasks

# Modelos de Negocio   

#READ
def check_tasks(id):    
    for task in tasks:
        if task.id == id:
            return task

    raise TaskNotFoundError(task_id=id)

#FIND
def task_id_exists(id):
    for task in tasks:
        if task.id == id:
            return True

    return False
    
#CREAT
def criar_task(task):
    task.id = len(tasks) + 1 
    if task_id_exists(task.id):
       raise DuplicateTaskError(task_id=task.id)
    
    tasks.append(task)
    return task



#DELETE
def delete_task(id):
    checkup = check_tasks(id)
    tasks.remove(checkup)
    
    