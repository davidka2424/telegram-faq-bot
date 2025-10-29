# Делаем функции доступными напрямую из пакета database
from .init_db import init_database, create_tables
from .db import find_similar_question, add_faq_item