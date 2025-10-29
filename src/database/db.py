import sqlite3
from typing import Optional, Tuple

def find_similar_question(db_path: str, user_query: str) -> Optional[Tuple[str, str]]:
    """
    Ищет похожий вопрос в БД по подстроке
    Возвращает кортеж (question, answer) или None
    """
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    cursor.execute(
        "SELECT question, answer FROM faq WHERE LOWER(question) LIKE LOWER(?)",
        (f'%{user_query}%',)
    )
    
    result = cursor.fetchone()
    conn.close()
    return result

def add_faq_item(db_path: str, question: str, answer: str):
    """Добавляет вопрос-ответ в БД"""
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    try:
        cursor.execute(
            "INSERT INTO faq (question, answer) VALUES (?, ?)",
            (question, answer)
        )
        conn.commit()
        print(f"✅ Добавлен вопрос: '{question}'")
    except sqlite3.IntegrityError:
        print(f"⚠️ Вопрос уже существует: '{question}'")
    finally:
        conn.close()