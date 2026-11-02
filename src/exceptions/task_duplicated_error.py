class DuplicateTaskError(Exception):
    """Execução para tarefas duplicadas"""
    def __init__(self, message: str = "Duplicate Task"):
        super().__init__(message)