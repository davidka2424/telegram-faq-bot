# 🤖 Telegram Echo & FAQ Bot

Простой Telegram-бот с эхо-функционалом и поиском по базе знаний FAQ. Написан на Python с использованием pyTelegramBotAPI.

## ✨ Функциональность

- **Эхо-ответ** - бот отвечает тем же сообщением
- **Поиск по FAQ** - команда `/faq <запрос>` ищет ответ в базе знаний
- **Docker-деплой** - готов к развертыванию на сервере

### 🚀 Быстрый старт

1. Клонирование репозитория

```bash
git clone https://github.com/davidka2424/telegram-faq-bot.git
cd telegram-faq-bot
2. Настройка окружения
Создайте файл .env в корне проекта:
```
```bash
cp .env_example .env
```
Отредактируйте .env файл, добавив ваш токен бота:
```
BOT_TOKEN=your_telegram_bot_token_here
```
Как получить токен:

Найти @BotFather в Telegram

Отправить команду /newbot

Следовать инструкциям и получить токен

3. Запуск с Docker (рекомендуется)
```bash
# Сборка и запуск контейнера
docker compose up -d

# Просмотр логов
docker compose logs -f telegram-bot
```
4. Запуск без Docker
```bash
# Установка зависимостей
pip install -r requirements.txt

# Инициализация базы данных
python scripts/fill_data.py

# Запуск бота
python src/bot.py
```
### 🏗 Структура проекта
```text
telegram-faq-bot/
├── src/                    # Исходный код
│   ├── bot.py             # Основная логика бота
│   ├── config.py          # Конфигурация
│   └── database/          # Работа с базой данных
│       ├── init_db.py     # Инициализация БД
│       └── db.py          # Операции с данными
├── scripts/
│   └── fill_data.py       # Заполнение БД тестовыми данными
├── data/                  # Директория для базы данных
├── docker-compose.yml     # Конфигурация Docker
├── Dockerfile             # Сборка Docker образа
├── requirements.txt       # Зависимости Python
└── .env.example          # Пример конфигурации
```
💻 Использование
После запуска бота:

Эхо-функция - отправьте любое сообщение, бот ответит тем же текстом

Поиск по FAQ - используйте команду:

```text
/faq Как оформить заказ?
/faq оплата
/faq доставка
```
### 🐳 Деплой на сервер
1. Подготовка сервера
```bash
# Установка Docker на Ubuntu
sudo apt update && sudo apt upgrade -y
sudo apt install docker.io docker-compose-plugin -y
sudo usermod -aG docker $USER
# Переподключиться к серверу
```
2. Развертывание проекта
```bash
# Клонирование проекта
git clone https://github.com/davidka2424/telegram-faq-bot.git
cd telegram-faq-bot

# Настройка окружения
echo "BOT_TOKEN=your_bot_token" > .env

# Запуск
docker compose up -d
```
3. Обновление кода
```bash
# На сервере
cd telegram-faq-bot
git pull
docker compose down
docker compose up -d --build
```
### 🛠 Команды управления
```bash
# Запуск
docker compose up -d

# Остановка
docker compose down

# Просмотр логов
docker compose logs -f telegram-bot

# Перезапуск
docker compose restart

# Обновление
docker compose up -d --build
```
📝 Тестовые данные
База знаний автоматически заполняется следующими вопросами:

"Как оформить заказ?"

"Какие способы оплаты вы принимаете?"

"Как отследить посылку?"

"Какой у вас график работы?"

"Что делать, если я забыл пароль?"

### 🔧 Разработка
Добавление новых вопросов в FAQ
Отредактируйте файл scripts/fill_data.py:

```python
SAMPLE_FAQ = [
    ("Ваш вопрос?", "Ответ на вопрос"),
    # ... остальные вопросы
]
```
Локальная разработка
```bash
# Установка зависимостей
pip install -r requirements.txt

# Запуск в режиме разработки
python src/bot.py
```
### 🐛 Решение проблем
Бот не отвечает
Проверьте токен в файле .env

Убедитесь что бот активирован в @BotFather

Проверьте логи: docker compose logs telegram-bot

Ошибки базы данных
Убедитесь что папка data/ существует и доступна для записи

Проверьте права доступа: chmod 755 data

Проблемы с Docker
Пересоберите образ: docker compose build --no-cache

Проверьте что Docker запущен: docker --version


Примечание: Не забудьте заменить your_telegram_bot_token_here на реальный токен от @BotFather!


## 🎯 **Ключевые разделы которые покрывает этот README:**

1. **Быстрый старт** - как быстро запустить проект
2. **Структура проекта** - обзор архитектуры  
3. **Деплой на сервер** - инструкция для продакшена
4. **Управление** - полезные команды Docker
5. **Разработка** - как расширять функционал
6. **Решение проблем** - частые ошибки и их исправление


