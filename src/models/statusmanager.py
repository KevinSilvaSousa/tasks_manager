from enum import Enum

class StatusManager(Enum):
    # GERENCIA OS STATUS DA TASK

    PENDENTE = "PENDENTE"
    EM_ANDAMENTO = "EM_ANDAMENTO"
    CONCLUIDA = "CONCLUIDA"
    CANCELADA = "CANCELADA"
