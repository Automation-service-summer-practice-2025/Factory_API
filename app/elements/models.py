from sqlalchemy import ForeignKey, text, Text
from sqlalchemy.orm import relationship, Mapped, mapped_column
from typing import List

from app.elements.schemas import SElement, SElementShort, SElementParams
from app.database import Base, str_uniq, int_pk, str_null_true, str_null_false
from datetime import date, datetime


class Element(Base):
    element_id: Mapped[int_pk]
    element_name: Mapped[str_null_false]
    certificate_number: Mapped[str_uniq]
    manufacturer_name: Mapped[str_null_false]
    passport_number: Mapped[int]
    factory_number: Mapped[int]
    date_last_metrological_control: Mapped[date]
    check_interval: Mapped[int]
    range_measurements: Mapped[str_null_false]
    date_last_check: Mapped[date]
    block_key_status: Mapped[bool]
    working_status: Mapped[bool]
    checking_date_start: Mapped[datetime]
    checking_date_finish: Mapped[datetime]

    station_id: Mapped[int] = mapped_column(ForeignKey("stations.station_id"), nullable=False)
    station: Mapped["Station"] = relationship("Station", back_populates="elements")

    documents: Mapped[List["Document"]] = relationship("Document", back_populates="element")

    def __str__(self):
        return f"{self.__class__.__name__}(id={self.element_id}, major_name={self.element_name!r})"

    def __repr__(self):
        return str(self)

    def to_schema(self) -> SElement:
        return SElement(
            element_id=self.element_id,
            element_name=self.element_name,
            station_id=self.station_id,
            params=SElementParams(
                manufacturer=self.manufacturer_name,
                passport=self.passport_number,
                factory=self.factory_number,
                certificate=self.certificate_number,
                interval_check=self.check_interval,
                last_metrological_control=self.date_last_metrological_control,
                last_check=self.date_last_check,
                range_measurement=self.range_measurements,
                block_key_status=self.block_key_status,
                working_status=self.working_status
            )
        )

    def to_schema_short(self) -> SElementShort:
        return SElementShort(
            element_id=self.element_id,
            element_name=self.element_name,
            working_status=self.working_status,
            checking_date_start=self.checking_date_start,
            checking_date_finish=self.checking_date_finish,
            block_key_status=self.block_key_status
        )
