class RBElement:
    def __init__(self, element_id: int | None = None,
                 element_name: str | None = None,
                 manufacturer: str | None = None,
                 working_status: bool | None = None,
                 passport_number: int | None = None,
                 certificate_number: str | None = None,
                 factory_number: int | None = None,
                 block_key_status: bool | None = None,
                 station_id: int | None = None,
                 check_interval: int | None = None):
        self.element_id = element_id
        self.element_name = element_name
        self.manufacturer = manufacturer
        self.working_status = working_status
        self.passport_number = passport_number
        self.certificate_number = certificate_number
        self.factory_number = factory_number
        self.block_key_status = block_key_status
        self.station_id = station_id
        self.check_interval = check_interval


    def to_dict(self) -> dict:
        data = {'element_id': self.element_id, 'element_name': self.element_name,
                'manufacturer': self.manufacturer,'working_status': self.working_status,
                'passport_number': self.passport_number,'certificate_number': self.certificate_number,
                'factory_number': self.factory_number,'block_key_status': self.block_key_status,
                'station_id': self.station_id,'check_interval': self.check_interval}
        # Создаем копию словаря, чтобы избежать изменения словаря во время итерации
        filtered_data = {key: value for key, value in data.items() if value is not None}
        return filtered_data