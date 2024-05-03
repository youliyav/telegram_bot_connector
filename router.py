from typing import Annotated

from fastapi import Depends
from fastapi import APIRouter
from repository import TaskRepository
from schemas import STask, STaskAdd, STaskId


router = APIRouter(
    prefix="/tasks",
    tags=["tasks"],
)

@router.post("")
async def add_task(task: Annotated[STaskAdd, Depends()],) -> STaskId:
    task_id = await TaskRepository.add_task(task)
    return {"ok": True, "task_id": task_id}  # type: ignore

@router.get("")
async def get_tasks() -> list[STask]:
    tasks = await TaskRepository.get_tasks()
    return tasks

