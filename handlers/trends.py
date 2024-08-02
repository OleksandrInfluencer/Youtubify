import logging
from aiogram import Router, types
from services.trends import get_trend_for_query
from .start import get_message
from utils.rate_limit import check_rate_limit

router = Router()

@router.callback_query(lambda c: c.data == 'shorts_trend')
async def process_shorts_trend(callback_query: types.CallbackQuery):
    await callback_query.message.answer(
        get_message(callback_query.from_user.id,
                    "Please enter a search query to get its popularity over the last week.",
                    "Будь ласка, введіть пошуковий запит для отримання його популярності за останній тиждень."))

@router.message()
async def handle_text_query(message: types.Message):
    if not check_rate_limit(message.from_user.id):
        await message.answer(get_message(message.from_user.id, "Too many requests. Please try again later.", "Занадто багато запитів. Будь ласка, спробуйте пізніше."))
        return

    try:
        query = message.text.strip()
        logging.info("Received query: %s", query)
        await message.answer(get_message(message.from_user.id,
                                         f"Getting data for query '{query}', please wait...",
                                         f"Отримую дані для запиту '{query}', будь ласка, зачекайте..."))

        trend = await get_trend_for_query(query)
        await message.answer(get_message(message.from_user.id,
                                         f"Popularity of query '{query}' over the last week: {trend}",
                                         f"Популярність запиту '{query}' за останній тиждень: {trend}"))
    except Exception as e:
        logging.error("Помилка при обробці запиту: %s", e, exc_info=True)
        await message.answer(get_message(message.from_user.id,
                                         "An error occurred while processing your query. Please try again later.",
                                         "Виникла помилка при обробці вашого запиту. Будь ласка, спробуйте пізніше."))

def register_trend_handlers(dp):
    dp.include_router(router)
