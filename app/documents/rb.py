class RBDocument:
    def __init__(self, document_id: int | None = None,
                 document_name: str | None = None,
                 element_id: int | None = None):
        self.document_id = document_id
        self.document_name = document_name
        self.element_id = element_id

    def to_dict(self) -> dict:
        data = {'document_id': self.document_id, 'document_name': self.document_name,
                'element_id': self.element_id}
        # Создаем копию словаря, чтобы избежать изменения словаря во время итерации
        filtered_data = {key: value for key, value in data.items() if value is not None}
        return filtered_data