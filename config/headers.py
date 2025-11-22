import os
from dotenv import load_dotenv

load_dotenv()

class Headers:
    # базовый header с токеном авторизации
    basic = {
        'Authorization': f'Bearer {os.getenv('API_TOKEN')}',
        'X-Task-Id': 'API-1'
    }
