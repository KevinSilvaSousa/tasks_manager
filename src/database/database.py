from sqlalchemy import Integer, String, ForeignKey, CheckConstraint, Boolean
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from src.models.statusmanager import StatusManager


# declarative base class
class Database(DeclarativeBase):
    pass



class Task(Database):
    __tablename__ = "tasks"

    task_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    task: Mapped[str] = mapped_column(String, nullable=False)
    completed: Mapped[str] = mapped_column(String, default=False, nullable=False)

    __table_args__ = (
        CheckConstraint(
            "completed IN ({StatusManager})",
            name="ck_tasks_completed_valid_values",
        ),
        CheckConstraint(
            "length(trim(task)) > 0",
            name="ck_tasks_task_not_blank",
        ),
    )


#ID gerado pelo banco.
#Descrição obrigatória.
#Status limitado aos quatro valores permitidos.
#Data de criação gerada automaticamente.