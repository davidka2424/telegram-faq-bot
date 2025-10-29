import os
from dotenv import load_dotenv

# Загружаем переменные из .env файла
load_dotenv()

# Токен бота из переменных окружения
BOT_TOKEN = os.getenv('BOT_TOKEN')

# Проверяем что токен есть
if not BOT_TOKEN:
    raise ValueError("BOT_TOKEN не найден! Создайте файл .env с вашим токеном")

# Путь к базе данных
DB_PATH = "data/faq.db"