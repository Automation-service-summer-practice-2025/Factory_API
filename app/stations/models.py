from sqlalchemy import ForeignKey, text, Text
from sqlalchemy.orm import relationship, Mapped, mapped_column
from typing import List

from app.database import Base, str_uniq, int_pk, str_null_true, str_null_false
from datetime import date


class Station(Base):
    station_id: Mapped[int_pk]
    station_name: Mapped[str_uniq]

    elements: Mapped[List["Element"]] = relationship("Element", back_populates="station")

    def __str__(self):
        return (f"{self.__class__.__name__}(id={self.station_id}, "
                f"first_name={self.station_name!r})")

    def __repr__(self):
        return str(self)
