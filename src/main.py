from fastapi import FastAPI
from src.api.routes.routes import router as task_router

from src.exceptions.exception_handlers import task_not_found_error, TaskNotFoundError

app = FastAPI(title = "Task Manager API",
    description = "Task Manager 1.0.0",
    version = "1.0.0")

app.include_router(task_router)

app.add_exception_handler(TaskNotFoundError ,task_not_found_error)