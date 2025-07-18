from datetime import datetime, date
from typing import Optional, List
import re
from pydantic import BaseModel, Field, EmailStr, validator
from app.elements.schemas import SElementShort


class SStation(BaseModel):
    station_id: int
    station_name: str = Field(..., description="Читаемое название установки")
    station_elements: List[SElementShort] = Field(None, description="Список агрегатов установки")

