class RBStation:
    def __init__(self, station_id: int | None = None,
                 station_name: int | None = None):
        self.station_id = station_id
        self.station_name = station_name

    def to_dict(self) -> dict:
        data = {'station_id': self.station_id, 'station_name': self.station_name}
        # Создаем копию словаря, чтобы избежать изменения словаря во время итерации
        filtered_data = {key: value for key, value in data.items() if value is not None}
        return filtered_data