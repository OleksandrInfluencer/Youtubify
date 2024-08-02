from aiogram import Router, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.filters import Command

# Зберігання вибору мови користувачів / Storing user language choices
user_languages = {}

def get_message(user_id, en_message, uk_message):
    language_code = user_languages.get(user_id, 'en')
    if language_code == 'uk':
        return uk_message
    return en_message

router = Router()

@router.message(Command('start'))
async def start_command(message: types.Message):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🇺🇦 Українська", callback_data='language_uk')],
        [InlineKeyboardButton(text="🇬🇧 English", callback_data='language_en')]
    ])
    await message.answer("Виберіть мову / Choose a language:", reply_markup=keyboard)

@router.callback_query(lambda c: c.data and c.data.startswith('language_'))
async def process_language_choice(callback_query: types.CallbackQuery):
    language_code = callback_query.data.split('_')[-1]
    user_id = callback_query.from_user.id
    user_languages[user_id] = language_code

    if language_code == 'uk':
        await callback_query.message.answer("Мову змінено на українську.")
    else:
        await callback_query.message.answer("Language changed to English.")

    # Відправити меню після вибору мови / Send menu after language selection
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=get_message(user_id, "Top Queries Hour", "Топ запити за годину"), callback_data='top_queries_hour')],
        [InlineKeyboardButton(text=get_message(user_id, "Top Queries Day", "Топ запити за день"), callback_data='top_queries_day')],
        [InlineKeyboardButton(text=get_message(user_id, "Top Queries Week", "Топ запити за тиждень"), callback_data='top_queries_week')],
        [InlineKeyboardButton(text=get_message(user_id, "Top Queries Month", "Топ запити за місяць"), callback_data='top_queries_month')],
        [InlineKeyboardButton(text=get_message(user_id, "Shorts Trend", "Тренди шортів"), callback_data='shorts_trend')]
    ])
    await callback_query.message.answer(get_message(user_id,
                            "Select one of the commands or enter a search query:",
                            "Виберіть одну з команд або введіть пошуковий запит:"), reply_markup=keyboard)

def register_start_handlers(dp):
    dp.include_router(router)
