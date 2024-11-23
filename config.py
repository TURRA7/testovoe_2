"""
Конфигурационный файл.

Notes:
    Получает данные из окружения(файла .env).
"""
import os
from dotenv import load_dotenv


load_dotenv()

TEXT = os.environ.get("...")
