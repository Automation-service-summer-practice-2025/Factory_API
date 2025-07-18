from fastapi import APIRouter, Depends
from sqlalchemy import select
from app.database import async_session_maker
from app.elements.models import Element
from app.elements.dao import ElementDAO
from app.elements.schemas import SElement
from app.elements.rb import RBElement

router = APIRouter(prefix='/elements', tags=["Работа с агрегатами"])


@router.get("/", summary="Получить список агрегатов")
async def get_all_elements(request_body: RBElement = Depends()) -> list[SElement]:
    elements = await ElementDAO.find_all(**request_body.to_dict())
    return [element.to_schema() for element in elements]

@router.get("/{id}", summary="Получить один агрегат по id")
async def get_student_by_id(element_id: int) -> SElement | dict:
    element = await ElementDAO.find_one_or_none_by_id(element_id)
    if element is None:
        return {'message': f'Агрегат с ID {element} не найден!'}
    return element.to_schema()