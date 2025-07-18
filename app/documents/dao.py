from app.dao.base import BaseDAO
from app.documents.models import Document


class DocumentDAO(BaseDAO):
    model = Document
