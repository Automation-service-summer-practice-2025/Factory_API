from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from datetime import datetime


class Model(DeclarativeBase):
   pass


class StationOrm(Model):
    __tablename__ = "stations"
    station_id: Mapped[int] = mapped_column(primary_key=True)
    station_name: Mapped[str]


class ElementOrm(Model):
   __tablename__ = "elements"
   element_id: Mapped[int] = mapped_column(primary_key=True)
   element_name: Mapped[str]
   certificate_number: Mapped[str]
   manufacturer_name: Mapped[str]
   passport_number: Mapped[int]
   factory_number: Mapped[int]
   date_last_metrological_control: Mapped[datetime]








