class DuplicateTaskError(Exception):
    """Execução para tarefas duplicadas"""
    def __init__(self, task_id, message: str = "Duplicate Task"):
        self.task_id = task_id
        super().__init__(message)


class TaskNotFoundError(Exception):
    """Exceção para tarefas nao encontradas."""
    def __init__(self,task_id,  message: str = "Task not found"):
        self.task_id = task_id
        super().__init__(message) 