from telegram import Bot
import os

bot = Bot(token=os.getenv("BOT_TOKEN"))
CHAT_ID = os.getenv("CHAT_ID")

async def send_message(text):
    await bot.send_message(chat_id=CHAT_ID, text=text)
