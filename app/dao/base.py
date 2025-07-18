from sqlalchemy.future import select
from app.database import async_session_maker


class BaseDAO:
    model = None

    @classmethod
    async def find_all(cls, **filter_by):
        async with async_session_maker() as session:
            query = select(cls.model).filter_by(**filter_by)
            result = await session.execute(query)
            return result.scalars().all()

    @classmethod
    async def find_one_or_none_by_id(cls, data_id: int):
        async with async_session_maker() as session:
            model_name = cls.model.__name__.lower()
            id_field = f"{model_name}_id"

            if not hasattr(cls.model, id_field):
                raise ValueError(f"Model {cls.model.__name__} has no field '{id_field}'")

            filter_kwargs = {id_field: data_id}
            query = select(cls.model).filter_by(**filter_kwargs)

            result = await session.execute(query)
            return result.scalar_one_or_none()
