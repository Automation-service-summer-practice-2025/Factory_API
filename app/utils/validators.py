from datetime import date, datetime


def validate_date_not_future(value: date | datetime | None, field_name: str):
    if value is None:
        return value

    # Приводим datetime к date
    if isinstance(value, datetime):
        value = value.date()

    if value > date.today():
        raise ValueError(f'Поле "{field_name}" не может быть в будущем')

    return value