from fastapi import FastAPI, HTTPException
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

@app.patch("/patch_tasks/{id}")
def patch_tasks(id: str, task_update: TaskUpdate):
        for task in tasks:


            if task.id == id:


                if "task" in task_update.model_fields_set:
                    task.task = task_update.task


                if "status" in task_update.model_fields_set:
                    task.status = task_update.status
                return task

            raise HTTPException(status_code=404, detail="Task not found")
