from fastapi import FastAPI
from data.tasks import tasks
from model.taskmodel import TaskModel
from model.taskupdate import TaskUpdate

# uvicorn main:app --reload

app = FastAPI(title = "Task Manager API",
    description = "A basic task manager",
    version = "1.0.0",)


@app.get("/search_tasks")
def search_tasks():
    return tasks


@app.post("/create_tasks")
def create_tasks(task: TaskModel):
    # Apos isso ela vai inserir a task dentro da lista
    # E por fim retornar a task
    tasks.append(task)
    return task


@app.delete("/delete_tasks/{id}")
def delete_tasks(id):

    for task in tasks:
        if task.id == id:
            tasks.remove()
            break

app.patch("/patch_tasks/{id}")
def patch_tasks(id, task_update: TaskUpdate):
        for task in tasks:
            if task.id == id:
                task_updated = task_update
                return task_updated
