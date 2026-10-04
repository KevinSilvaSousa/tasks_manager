from fastapi import FastAPI

app = FastAPI(title = "Task Manager API",
    description = "A basic task manager",
    version = "1.0.0",)

@app.get("/")
def root():
    return {"message": "Hello World"}


@app.get("/search_tasks")
def search_tasks():
    # 1 - Precisa buscar as tasks no codigo, 
    # 2 - Precisa acessar o banco de dados onde possivelmente estao as tasks
    #  
    return {"message": "This route is used to search for tasks"}