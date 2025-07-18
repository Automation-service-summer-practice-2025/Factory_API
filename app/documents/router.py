from fastapi import APIRouter, Depends
from sqlalchemy import select
from app.database import async_session_maker
from app.documents.dao import DocumentDAO
from app.documents.rb import RBDocument
from app.documents.schemas import SDocument

router = APIRouter(prefix='/documents', tags=["Работа с актами"])


@router.get("/", summary="Получить список всех актов")
async def get_all_documents(request_body: RBDocument = Depends()) -> list[SDocument]:
    return await DocumentDAO.find_all(**request_body.to_dict())
