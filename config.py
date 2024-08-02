from dotenv import load_dotenv
import os

# Завантаження змінних середовища / Load environment variables
load_dotenv()

TELEGRAM_API_KEY = os.getenv('TELEGRAM_API_KEY')
YOUTUBE_API_KEY = os.getenv('YOUTUBE_API_KEY')
