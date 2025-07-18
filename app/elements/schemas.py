from datetime import datetime, date
from typing import Optional, Union, List
import re
from pydantic import BaseModel, Field, validator, model_validator
from app.utils.validators import validate_date_not_future
from app.documents.schemas import SDocument


class SElementParams(BaseModel):
    manufacturer: str = Field(..., description="Изготовитель")
    passport: int = Field(..., description="Номер паспорта")
    factory: int = Field(..., description="Заводской №")
    certificate: str = Field(..., description="Номер свидетельства ФГИС Аршин")
    interval_check: int = Field(..., description="Межповерочный интервал, год")
    last_metrological_control: datetime = Field(..., description="Дата последнего метрологического контроля")
    last_check: datetime = Field(..., description="Дата последней поверки")
    range_measurement: str = Field(..., description="Диапазон измерений НКПР компонента, %")
    block_key_status: bool = Field(..., description="Состояние деблокировки")
    working_status: bool = Field(..., description="Статус работы")

    @model_validator(mode='after')
    def validate_dates(self):
        validate_date_not_future(self.last_metrological_control, 'date_last_metrological_control')
        validate_date_not_future(self.last_check, 'last_check')
        return self


class SElement(BaseModel):
    element_id: int
    element_name: str = Field(..., description="Читаемое название агрегата")
    station_id: int = Field(..., description="Номер установки в которой находится агрегат")
    params: SElementParams = Field(..., description="Параметры агрегата")
    documents: List[SDocument] = Field(None, description="Список актов на агрегат")


class SElementShort(BaseModel):
    element_id: int
    element_name: str = Field(..., description="Название элемента")
    working_status: bool = Field(..., description="Статус работы")
    checking_date_start: date = Field(..., description="Дата начала проверки агрегата в формате ГГГГ-ММ-ДД")
    checking_date_finish: date = Field(..., description="Дата конца проверки агрегата в формате ГГГГ-ММ-ДД")
    block_key_status: bool = Field(..., description="Статус работы")

    @model_validator(mode='after')
    def validate_dates(self):
        validate_date_not_future(self.date_last_metrological_control, 'date_last_metrological_control')
        validate_date_not_future(self.checking_date_start, 'checking_date_start')
        validate_date_not_future(self.checking_date_finish, 'checking_date_finish')
        return self
