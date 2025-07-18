from fastapi import APIRouter, Depends
from sqlalchemy import select
from app.database import async_session_maker
from app.stations.models import Station
from app.stations.dao import StationDAO
from app.stations.schemas import SStation
from app.stations.rb import RBStation

router = APIRouter(prefix='/stations', tags=["Работа с установками"])


@router.get("/", summary="Получить список установок")
async def get_all_stations(request_body: RBStation = Depends()) -> list[SStation]:
    return await StationDAO.find_all(**request_body.to_dict())


@router.get("/{id}", summary="Получить одну установку по id")
async def get_student_by_id(station_id: int) -> SStation | dict:
    station = await StationDAO.find_one_or_none_by_id(station_id)
    if station is None:
        return {'message': f'Установка с ID {station_id} не найдена!'}
    return station
