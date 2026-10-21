from fastapi import FastAPI
from src.api.routes.routes import router as task_router

# python -m uvicorn src.main:app --reload

app = FastAPI(title = "Task Manager API",
    description = "A basic task manager",
    version = "1.0.0")

app.include_router(task_router)





