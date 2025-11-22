from services.users.api_users import UsersAPI


class BaseTest:
    # здесь будем создавать объекты API-сервисов, что даст нам доступ ко всем сервисам из любого файла
    def setup_method(self):
        self.api_users = UsersAPI()