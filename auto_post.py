from aiogram import Bot
from data import config
import asyncio

bot = Bot(token=config.BOT_TOKEN)

async def post_to_channel(channel_id: int, message_text: str):
    try:
        await bot.send_message(chat_id=channel_id, text=message_text)
        print(f"Message sent to channel {channel_id}")
    except Exception as e:
        print(f"Error sending message to channel: {e}")

async def scheduled_posts(channel_id: int, interval: int):
    while True:
        await post_to_channel(channel_id, "Bu avtomatik xabar.")
        await asyncio.sleep(interval)
