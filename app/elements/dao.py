from sqlalchemy import select
from app.elements.models import Element
from app.database import async_session_maker
from app.dao.base import BaseDAO


class ElementDAO(BaseDAO):
    model = Element
