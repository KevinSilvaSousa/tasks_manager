class TaskNotFoundError(Exception):
    """Exceção para tarefas nao encontradas."""
    def __init__(self, message: str = "Task not found"):
        super().__init__(message) 