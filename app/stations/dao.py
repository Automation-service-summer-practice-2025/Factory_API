from app.dao.base import BaseDAO
from app.stations.models import Station


class StationDAO(BaseDAO):
    model = Station
