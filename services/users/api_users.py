# здесь хранятся методы сервиса Users
from utils.helper import Helper
from services.users.endpoints import Endpoints
from services.users.payloads import Payloads
from config.headers import Headers
import requests
import allure
from services.users.models.user_model import UserModel

# наследуемся от Helper, чтобы в API-методах мы могли воспользоваться методом attach_response
class UsersAPI(Helper):

    def __init__(self):
        super().__init__()
        self.payloads = Payloads()
        self.endpoints = Endpoints()
        self.headers = Headers()

    # метод создания юзера
    @allure.step('Create user')
    def create_user(self):
        response = requests.post(
            url = self.endpoints.create_user,
            headers = self.headers.basic,
            json = self.payloads.create_user
        )
        assert response.status_code == 200, response.json()
        self.attach_response(response.json()) # прикрепляем json к allure-отчету
        model = UserModel(**response.json())
        return model # теперь в тесте получаем доступ к полям модели

    @allure.step('Get user by ID')
    def get_user_by_id(self, uuid):
        response = requests.get(
            url=self.endpoints.get_user_by_id(uuid),
            headers=self.headers.basic
        )
        assert response.status_code == 200, response.json()
        self.attach_response(response.json())  # прикрепляем json к allure-отчету
        model = UserModel(**response.json())
        return model  # теперь в тесте получаем доступ к полям модели
