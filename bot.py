import logging
import asyncio
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from config import TELEGRAM_API_KEY
from handlers import register_handlers

# Встановлення логування / Set up logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.ERROR  # Зміна рівня логування на ERROR / Change log level to ERROR
)

# Окремий логер для критичних подій / Separate logger for critical events
critical_logger = logging.getLogger('critical_logger')
critical_logger.setLevel(logging.INFO)
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
critical_logger.addHandler(ch)

# Ініціалізація бота та диспетчера / Initialize bot and dispatcher
bot = Bot(token=TELEGRAM_API_KEY)
dp = Dispatcher(storage=MemoryStorage())

# Налаштування обробників / Set up handlers
register_handlers(dp)

async def main():
    critical_logger.info("Bot started")  # Лог повідомлення про запуск бота / Log message about bot start
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
