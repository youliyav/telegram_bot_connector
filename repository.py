from sqlalchemy import select
from database import TaskOrm, new_session
from schemas import STaskAdd, STask


class TaskRepository:
    @classmethod
    async def add_task(cls, task: STaskAdd) -> int:  # принимает не случайный словарь, а Pydantic-схему
        async with new_session() as session:  # асинхр. контекстный менеджер автоматически закрывает сессию (не нужен session.close())
            data = task.model_dump()  # model_dump() - преобразует схему в словарь
            new_task = TaskOrm(**data)  # TaskOrm(dict) - создает новую задачу, хранит ее внутри FastAPI.
            session.add(new_task)  # add() - добавляет задачу в объект сессии, чтобы SQLAlchemy знала, какие изменения отпр. в БД

            # flush() - отпр. в БД SQL запрос `INSERT INTO tasks (name, description) VALUES ("Task_1", NULL) RETURNING id`
            # и позволяет получить значение столбца id новой задачи.
            await session.flush()
            await session.commit()  # commit() - фиксирует изменения в БД, завершая транзакцию.
            return new_task.id  # Возвращает ID задачи

    @classmethod
    async def get_tasks(cls) -> list[STask]:

        async with new_session() as session:
            # SQLAlchemy конвертирует ответ от БД к экземплярам модели TaskOrm
            query = select(TaskOrm)  # запрос типа SELECT из sqlalchemy, отдаст все строки из БД
            result = await session.execute(query)  # result — итератор
            task_models = result.scalars().all()  # scalars().all() исп., чтобы выбрать все нужные результаты
            tasks = [STask.model_validate(task_model) for task_model in task_models]
            return tasks
