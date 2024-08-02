# Telegram Bot

## Опис бота / Bot Description

**Українською:**
Цей Telegram бот дозволяє користувачам вибирати мову (українську або англійську) і отримувати популярні запити з YouTube та тренди шортів на основі введених ключових слів. Бот підтримує відправку запитів для отримання популярних відео за останню годину, день, тиждень або місяць.

**English:**
This Telegram bot allows users to choose a language (Ukrainian or English) and receive popular queries from YouTube and shorts trends based on entered keywords. The bot supports sending requests to get popular videos from the last hour, day, week, or month.

## Інструкція по запуску бота / Bot Launch Instructions

**Українською:**
1. Встановіть Python 3.7 або вище.
2. Встановіть залежності, виконавши команду `pip install -r requirements.txt`.
3. Отримайте ключі API для Telegram та YouTube.
4. Створіть файл `.env` у корені проекту та додайте ваші ключі API:
    ```
    TELEGRAM_API_KEY=your_telegram_api_key
    YOUTUBE_API_KEY=your_youtube_api_key
    ```
5. Запустіть бот командою `python bot.py`.

**English:**
1. Install Python 3.7 or higher.
2. Install dependencies by running `pip install -r requirements.txt`.
3. Obtain API keys for Telegram and YouTube.
4. Create a `.env` file in the root of the project and add your API keys:
    ```
    TELEGRAM_API_KEY=your_telegram_api_key
    YOUTUBE_API_KEY=your_youtube_api_key
    ```
5. Run the bot with the command `python bot.py`.
