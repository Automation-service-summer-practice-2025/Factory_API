from sqlalchemy import select
from app.elements.models import Element
from app.database import async_session_maker
from app.dao.base import BaseDAO
from app.elements.schemas import SElement, SElementParams
from app.documents.models import Document


class ElementDAO(BaseDAO):
    model = Element


    @classmethod
    async def find_full_data(cls, element_id: int) -> SElement | None:
        async with async_session_maker() as session:

            query_elemnet = select(cls.model).filter_by(element_id=element_id)
            result_element = await session.execute(query_elemnet)
            element_info = result_element.scalar_one_or_none()

            if not element_info:
                return None

            query_documents = select(Document).filter_by(element_id=element_info.element_id)
            result_documents = await session.execute(query_documents)

            if result_documents is None:
                return SElement(
                    element_id=element_info.element_id,
                    element_name=element_info.element_name,
                    station_id=element_info.station_id,
                    params=SElementParams(
                        manufacturer=element_info.manufacturer_name,
                        passport=element_info.passport_number,
                        factory=element_info.factory_number,
                        certificate=element_info.certificate_number,
                        interval_check=element_info.check_interval,
                        last_metrological_control=element_info.date_last_metrological_control,
                        last_check=element_info.date_last_check,
                        range_measurement=element_info.range_measurements,
                        block_key_status=element_info.block_key_status,
                        working_status=element_info.working_status
                        )
                    )

            documents = result_documents.scalars().all()
            return SElement(
                element_id=element_info.element_id,
                element_name=element_info.element_name,
                station_id=element_info.station_id,
                params=SElementParams(
                    manufacturer=element_info.manufacturer_name,
                    passport=element_info.passport_number,
                    factory=element_info.factory_number,
                    certificate=element_info.certificate_number,
                    interval_check=element_info.check_interval,
                    last_metrological_control=element_info.date_last_metrological_control,
                    last_check=element_info.date_last_check,
                    range_measurement=element_info.range_measurements,
                    block_key_status=element_info.block_key_status,
                    working_status=element_info.working_status
                ),
                documents=[document.to_schema_short() for document in documents]
            )