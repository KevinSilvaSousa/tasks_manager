from fastapi import Request
from fastapi.responses import JSONResponse

from src.exceptions.errors import * 



def task_not_found_error(request: Request, exc: TaskNotFoundError):
    return JSONResponse(
        status_code=404,
        content={
            "erro": "Not Found",
            "detail": f"O recurso com o ID: `{exc.task_id}` não foi encontrado: `{exc.args[0]}`.",
            "path": request.url.path # Informação útil extraída do objeto Request
    })



def duplicate_task_error(request: Request, exc: DuplicateTaskError):
    return JSONResponse(
        status_code=409,
        content={
            "erro": "duplicate task",
            "detail": f"O recurso com o ID: `{exc.task_id}` ja existe: `{exc.args[0]}`."
        })