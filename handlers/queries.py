import logging
from aiogram import Router, types
from services.youtube import get_top_queries, format_views
from .start import get_message, user_languages

router = Router()

@router.callback_query(lambda c: c.data and c.data.startswith('top_queries_'))
async def process_top_queries(callback_query: types.CallbackQuery):
    period = callback_query.data.split('_')[-1]
    queries = await get_top_queries(period)
    await send_queries(callback_query.message, queries, callback_query.from_user.id)

async def send_queries(message: types.Message, queries, user_id):
    language_code = user_languages.get(user_id, 'en')
    max_length = 4096  # Максимальна довжина повідомлення в Telegram / Maximum message length in Telegram
    formatted_queries = "\n".join(
        [f"{i + 1}. [{query[0]}](https://www.youtube.com/watch?v={query[2]}) - {format_views(query[1], language_code)}" for i, query in enumerate(queries)]
    )
    for i in range(0, len(formatted_queries), max_length):
        await message.answer(formatted_queries[i:i + max_length], parse_mode='Markdown')

def register_query_handlers(dp):
    dp.include_router(router)
