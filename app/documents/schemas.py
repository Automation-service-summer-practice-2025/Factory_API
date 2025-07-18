from datetime import datetime, date
from typing import Optional
import re
from pydantic import BaseModel, Field, EmailStr, validator


class SDocument(BaseModel):
    document_id: int
    document_name: str = Field(..., description="Название документа")
    element_id: int = Field(..., description="Номер агрегата, к которому относится акт")

class SDocumentShort(BaseModel):
    document_id: int
    document_name: str = Field(..., description="Название документа")