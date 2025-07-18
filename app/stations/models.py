from sqlalchemy import ForeignKey, text, Text
from sqlalchemy.orm import relationship, Mapped, mapped_column
from app.database import Base, str_uniq, int_pk, str_null_true, str_null_false
from datetime import date


class Station(Base):
    station_id: Mapped[int_pk]
    station_name: Mapped[str_uniq]

    def __str__(self):
        return (f"{self.__class__.__name__}(id={self.station_id}, "
                f"first_name={self.station_name!r})")

    def __repr__(self):
        return str(self)


class Element(Base):
    element_id: Mapped[int_pk]
    element_name: Mapped[str_null_false]
    certificate_number: Mapped[str_uniq]
    manufacturer_name: Mapped[str_null_false]
    passport_number: Mapped[str_uniq]
    factory_number: Mapped[str_null_false]
    date_last_metrological_control: Mapped[date]
    check_interval: Mapped[int]
    range_measurements: Mapped[str_null_false]
    date_last_check: Mapped[date]
    block_key_status: Mapped[bool]
    working_status: Mapped[bool]
    checking_date_start: Mapped[date]
    checking_date_finish: Mapped[date]

    station_id: Mapped[int] = mapped_column(ForeignKey("stations.id"), nullable=False)
    station: Mapped["Station"] = relationship("Station", back_populates="elements")

    def __str__(self):
        return f"{self.__class__.__name__}(id={self.element_id}, major_name={self.element_name!r})"

    def __repr__(self):
        return str(self)


class Document(Base):
    document_id: Mapped[int_pk]
    document_name: Mapped[str_uniq]

    element_id: Mapped[int] = mapped_column(ForeignKey("elements.id"), nullable=False)
    element: Mapped["Element"] = relationship("Element", back_populates="documents")

    def __str__(self):
        return (f"{self.__class__.__name__}(id={self.document_id}, "
                f"first_name={self.document_name!r})")

    def __repr__(self):
        return str(self)