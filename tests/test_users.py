from config.base_test import BaseTest
import allure
import pytest


@allure.epic('Administration')
@allure.feature('Users')
class TestUsers(BaseTest):

    @pytest.mark.users
    @allure.title('Create new user')
    def test_create_user(self):
        user = self.api_users.create_user()
        print(self.api_users.get_user_by_id(user.uuid)) # в этот запрос передаем данные из предыдущего запроса