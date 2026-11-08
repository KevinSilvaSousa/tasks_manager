from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse

from src.exceptions.errors import * 

from src.main import app



def task_not_found_error(request: Request, exc: TaskNotFoundError):
    return JSONResponse(
        status_code=404,
        content={
            "erro": "Not Found",
            "detalhes": f"O recurso com o ID: `{exc.task_id}` não foi encontrado: `{exc.args[0]}`.",
            "path": request.url.path # Informação útil extraída do objeto Request
    })
