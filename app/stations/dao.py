from app.dao.base import BaseDAO
from app.stations.models import Station
from app.elements.models import Element
from app.database import async_session_maker
from sqlalchemy.future import select
from app.stations.schemas import SStation


class StationDAO(BaseDAO):
    model = Station

    @classmethod
    async def find_full_data(cls, station_id: int) -> SStation | None:
        async with async_session_maker() as session:

            query_station = select(cls.model).filter_by(station_id=station_id)
            result_station = await session.execute(query_station)
            station_info = result_station.scalar_one_or_none()

            if not station_info:
                return None

            query_elements = select(Element).filter_by(station_id=station_info.station_id)
            result_elements = await session.execute(query_elements)

            if result_elements is None:
                return SStation(
                    station_id=station_info.station_id,
                    station_name=station_info.station_name,
                    )

            elements = result_elements.scalars().all()
            return SStation(
                station_id=station_info.station_id,
                station_name=station_info.station_name,
                station_elements=[element.to_schema_short() for element in elements]
            )