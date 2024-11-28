from aiogram import executor, types
from loader import dp
from data import config
import asyncio

async def on_startup(dispatcher):
    print("Bot ishga tushdi!")

# Botga har qanday turdagi xabar kelganda ishlov berish
@dp.message_handler(content_types=types.ContentType.ANY)
async def send_post_to_channel(message: types.Message):
    # Har qanday turdagi xabarni belgilangan kanalga yuborish
    if message.text:  # Agar xabar matn bo'lsa
        await message.bot.send_message(config.CHANNEL_IDS, message.text)
    elif message.photo:  # Agar rasm bo'lsa
        await message.bot.send_photo(config.CHANNEL_IDS, message.photo[-1].file_id, caption=message.caption)
    elif message.video:  # Agar video bo'lsa
        await message.bot.send_video(config.CHANNEL_IDS, message.video.file_id, caption=message.caption)
    elif message.document:  # Agar fayl bo'lsa
        await message.bot.send_document(config.CHANNEL_IDS, message.document.file_id, caption=message.caption)

if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)

