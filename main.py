from fastapi import FastAPI
from data.tasks import tasks
from model.taskmodel import TaskModel

# uvicorn main:app --reload

app = FastAPI(title = "Task Manager API",
    description = "A basic task manager",
    version = "1.0.0",)


@app.get("/search_tasks")
def search_tasks():
    # 1 - Precisa buscar as tasks no codigo, 
    # 2 - Precisa acessar o banco de dados onde possivelmente estao as tasks
    # 3 - 

    return tasks


@app.post("/create_tasks")
def create_tasks(task: TaskModel):
    # Apos isso ela vai inserir a task dentro da lista
    # E por fim retornar a task
    tasks.append(task)
    return task


@app.delete("/delete_tasks/{id}")
def delete_tasks(id,):

    for task in tasks:
        if task.id == id:
            tasks.remove()
            break