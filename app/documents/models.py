from sqlalchemy import ForeignKey, text, Text
from sqlalchemy.orm import relationship, Mapped, mapped_column
from typing import List

from app.database import Base, str_uniq, int_pk, str_null_true, str_null_false
from datetime import date
from app.documents.schemas import SDocumentShort


class Document(Base):
    document_id: Mapped[int_pk]
    document_name: Mapped[str_uniq]

    element_id: Mapped[int] = mapped_column(ForeignKey("elements.element_id"), nullable=False)
    element: Mapped["Element"] = relationship("Element", back_populates="documents")

    def __str__(self):
        return (f"{self.__class__.__name__}(id={self.document_id}, "
                f"first_name={self.document_name!r})")

    def __repr__(self):
        return str(self)

    def to_schema_short(self) -> SDocumentShort:
        return SDocumentShort(
            document_id=self.document_id,
            document_name=self.document_name
        )