import os
from dotenv import load_dotenv

# .env faylini yuklash
load_dotenv('D:/django_project/Kanallar-bilan-ishlash/.env')

# O'zgaruvchilarni yuklash
BOT_TOKEN = os.getenv("BOT_TOKEN")
ADMINS = list(map(int, os.getenv("ADMINS").split(',')))

# CHANNEL_IDS ni list shaklida yuklash
CHANNEL_IDS = os.getenv("CHANNEL_IDS")
if CHANNEL_IDS:
    # Har bir channel_id ni int ga aylantirish
    try:
        CHANNEL_IDS = [int(channel_id.strip()) for channel_id in CHANNEL_IDS.split(',')]
    except ValueError:
        raise ValueError("CHANNEL_IDS noto'g'ri formatda, int ga aylantirib bo'lmaydi.")
else:
    raise ValueError("CHANNEL_IDS .env faylida aniqlanmagan.")

IP = os.getenv("ip")
