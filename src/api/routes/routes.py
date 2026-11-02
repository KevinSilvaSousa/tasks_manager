# IMPORT FASTAPI
from fastapi import HTTPException, APIRouter, status

# IMPORT DO BANDO DE DADOS
from src.data.tasks import tasks

# IMPORT DO MODELO
from src.models.taskmodel import TaskModel
from src.models.taskupdate import TaskUpdate
from src.models.message_response_model import MessageResponse   

# IMPORT DE EXCESSOES
from src.exceptions.task_duplicated_error import DuplicateTaskError 


# IMPORT DAS REGRAS DE NEGOCIOS

from src.services.task_service import *



router = APIRouter()

# TASK SEARCH ROUTE
@router.get("/search_tasks", response_model=list[TaskModel])
def search_tasks():
        return tasks


# TASK FIND ROUTE 
@router.get("/find_task/{id}", response_model=TaskModel)

def find_task(id: int):
    for task in tasks:
        if task.id == id:
            return task
    else:
        raise HTTPException(status_code=404, detail="Task not found") 


# TASK CREATE ROUTE 
@router.post("/create_tasks", response_model=TaskModel)
def create_tasks(task: TaskModel):
    # Apos isso ela vai inserir a task dentro da lista
    # E por fim retornar a task
    task.id = len(tasks) + 1 
    if task_id_exists(task.id):
        raise DuplicateTaskError 
    
    tasks.append(task)
    return task


# TASK DELETE ROUTE
@router.delete("/delete_tasks/{id}", response_model=MessageResponse)
def delete_tasks(id):

    for task in tasks:
        if task.id == id:
            tasks.remove(id)
            break
    else:
        return {"message": "Task not found"}



# TASK PATCH ROUTE
@router.patch("/patch_tasks/{id}", response_model=TaskModel)
def patch_tasks(id: int, task_update: TaskUpdate):
    for task in tasks:

        if task.id == id:

            if "task" in task_update.model_fields_set:
                task.task = task_update.task

            if "status" in task_update.model_fields_set:
                task.status = task_update.status
            return task

    raise HTTPException(status_code=404, detail="Task not found")