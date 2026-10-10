from fastapi import FastAPI
from routes.routes import *

# uvicorn main:app --reload

app = FastAPI(title = "Task Manager API",
    description = "A basic task manager",
    version = "1.0.0",)


