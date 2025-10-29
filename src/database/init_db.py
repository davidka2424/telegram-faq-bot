# import sqlite3
# import os
# from pathlib import Path

# def create_tables(db_path: str):
#     """Создает таблицы в базе данных"""
#     conn = sqlite3.connect(db_path)
#     cursor = conn.cursor()
    
#     cursor.execute('''
#         CREATE TABLE IF NOT EXISTS faq (
#             id INTEGER PRIMARY KEY AUTOINCREMENT,
#             question TEXT NOT NULL,
#             answer TEXT NOT NULL
#         )
#     ''')
    
#     conn.commit()
#     conn.close()
#     print(f"✅ Таблицы созданы в {db_path}")

# def init_database(db_path: str):
#     """Инициализирует базу данных: создает папку и таблицы"""
#     # Создаем папку data если её нет
#     os.makedirs(os.path.dirname(db_path), exist_ok=True)
    
#     # Создаем таблицы
#     create_tables(db_path)


#!/usr/bin/env python3
"""
Скрипт для заполнения базы данных тестовыми вопросами
"""

import sys
import os
from pathlib import Path

# Добавляем src в путь для импорта
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

# Теперь можно импортировать модули из src
from src.config import DB_PATH
from src.database.init_db import init_database
from src.database.db import add_faq_item

# Тестовые данные
SAMPLE_FAQ = [
    ("Как оформить заказ?", "Вы можете оформить заказ через корзину на нашем сайте."),
    ("Какие способы оплаты вы принимаете?", "Мы принимаем карты Visa, MasterCard, МИР и наличные при получении."),
    ("Как отследить посылку?", "Отследить посылку можно по трек-номеру в вашем личном кабинете."),
    ("Какой у вас график работы?", "Мы работаем с 8:00 до 18:00 по московскому времени, без выходных."),
    ("Что делать, если я забыл пароль?", "Воспользуйтесь функцией 'Восстановление пароля' на странице входа."),
]

def main():
    """Заполняет базу тестовыми данными"""
    print("🔄 Заполняем базу знаний тестовыми данными...")
    
    # Инициализируем БД (создаем таблицы)
    init_database(DB_PATH)
    
    # Добавляем вопросы
    for question, answer in SAMPLE_FAQ:
        add_faq_item(DB_PATH, question, answer)
    
    print(f"✅ База знаний заполнена! Добавлено {len(SAMPLE_FAQ)} вопросов.")

if __name__ == "__main__":
    main()