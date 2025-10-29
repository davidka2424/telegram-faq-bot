import telebot
from config import BOT_TOKEN, DB_PATH
from database import init_database, find_similar_question

# Создаем экземпляр бота
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    """Обработчик команды /start"""
    welcome_text = """
🤖 Привет! Я эхо-бот с базой знаний FAQ.

Просто напиши мне что-нибудь, и я отвечу тем же.

Используй команду:
/faq <вопрос> - для поиска в базе знаний

Пример: 
/faq Как оформить заказ?
/faq оплата
    """
    bot.reply_to(message, welcome_text)

@bot.message_handler(commands=['faq'])
def handle_faq(message):
    """Обработчик команды /faq"""
    # Получаем текст после команды /faq
    command_text = message.text.strip()
    
    if command_text == '/faq':
        bot.reply_to(
            message, 
            "Пожалуйста, укажите вопрос после команды.\nПример: /faq Как оформить заказ?"
        )
        return
    
    # Извлекаем запрос (убираем '/faq ' из начала строки)
    user_query = command_text[5:].strip().lower().capitalize()
    
    if not user_query:
        bot.reply_to(message, "Введите вопрос для поиска после команды /faq")
        return
    
    # Ищем в базе данных
    result = find_similar_question(DB_PATH, user_query)
    
    if result:
        question, answer = result
        response = f"❓ Вопрос: {question}\n\n✅ Ответ: {answer}"
    else:
        response = "К сожалению, я не нашел ответа на ваш вопрос."
    
    bot.reply_to(message, response)

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    """Эхо-обработчик для всех текстовых сообщений"""
    # Игнорируем команды
    if message.text.startswith('/'):
        return
    
    # Отвечаем тем же текстом
    bot.reply_to(message, message.text)

def main():
    """Запускает бота"""
    # Инициализируем базу данных
    init_database(DB_PATH)
    
    # Запускаем бота
    print("🤖 Бот запущен...")
    bot.infinity_polling()

if __name__ == "__main__":
    main()