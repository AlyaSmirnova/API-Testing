# здесь вызываем метод setup, чтобы поднять окружение (чистит БД и заново поднимает окружение)
# фикстура будет вызываться для сессии (один раз для всех тестов)
import os
from dotenv import load_dotenv # подгрузит переменные окружения
import requests
import pytest

# подгружает из файла .env значение API_TOKEN
load_dotenv()

# для запуска на нескольких стендах
HOST = 'https://dev-gs.qa-playground.com/api/v1' if os.environ["STAGE"] == 'qa' else 'https://release-gs.qa-playground.com/api/v1'

# фикстура для инициализации окружения
@pytest.fixture(autouse=True, scope='session')
def init_environment():
    response = requests.post(
        url = f'{HOST}/setup',
        headers = {"Authorization': f'Bearer {os.getenv('API_TOKEN')}"}
    )
    assert response.status_code == 205