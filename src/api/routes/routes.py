from fastapi import HTTPException, APIRouter, status
from src.data.tasks import tasks
from src.models.taskmodel import TaskModel
from src.models.taskupdate import TaskUpdate

router = APIRouter()

@router.get("/search_tasks")
def search_tasks():
        return tasks


@router.get("/find_task/{id}")
def find_task(id: int):
    for task in tasks:
        if task.id == id:
            return task
    else:
        raise HTTPException(status_code=404, detail="Task not found") 


@router.post("/create_tasks")
def create_tasks(task: TaskModel):
    # Apos isso ela vai inserir a task dentro da lista
    # E por fim retornar a task
    if task.id == task.id:
        raise  HTTPException(status_code=status.HTTP_409_CONFLICT,detail=f"O ID {task.id} já existe.")

    else:
        tasks.append(task)
    
    return task


@router.delete("/delete_tasks/{id}")
def delete_tasks(id):

    for task in tasks:
        if task.id == id:
            tasks.remove(id)
            break
    else:
        return {"message": "Task not found"}

@router.patch("/patch_tasks/{id}")
def patch_tasks(id: int, task_update: TaskUpdate):
    for task in tasks:

        if task.id == id:

            if "task" in task_update.model_fields_set:
                task.task = task_update.task

            if "status" in task_update.model_fields_set:
                task.status = task_update.status
            return task

    raise HTTPException(status_code=404, detail="Task not found")