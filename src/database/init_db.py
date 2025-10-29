import sqlite3
import os
from pathlib import Path

def create_tables(db_path: str):
    """Создает таблицы в базе данных"""
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS faq (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            question TEXT NOT NULL,
            answer TEXT NOT NULL
        )
    ''')
    
    conn.commit()
    conn.close()
    print(f"✅ Таблицы созданы в {db_path}")

def init_database(db_path: str):
    """Инициализирует базу данных: создает папку и таблицы"""
    # Создаем папку data если её нет
    os.makedirs(os.path.dirname(db_path), exist_ok=True)
    
    # Создаем таблицы
    create_tables(db_path)