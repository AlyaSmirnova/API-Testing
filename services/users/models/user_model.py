from pydantic import BaseModel, field_validator


class UserModel(BaseModel):
    # описываем модель ответа: в ответе должны прийти следующие поля и тип данных в них
    email: str
    name: str
    nickname: str
    uuid: str

    # пишем кастомный валидатор: проверяем, что поля не пустые
    @field_validator('email', 'name', 'nickname', 'uuid') # декоратор pydantic
    def fields_are_not_empty(cls, value):
        if value == '' or value is None:
            raise ValueError('Field is empty')
        else:
            return value