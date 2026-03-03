import asyncio
from aiogram import Bot, Dispatcher, F, types

TOKEN = "8719477941:AAGg0tfoOM9vi4wtIuXDEAtAwHDgfIq4jt8" 
CHANNEL_ID = -1003773267126 

bot = Bot(token=TOKEN)
dp = Dispatcher()


@dp.message()
async def handle_message(message: types.Message):
    if str(message.chat.id) == str(CHANNEL_ID):
        await process_post(message)

@dp.channel_post()
async def handle_channel_post(message: types.Message):
    if str(message.chat.id) == str(CHANNEL_ID):
        await process_post(message)

async def process_post(message: types.Message):
    content = message.text or message.caption or "Без тексту"
    print(f"--- Нове повідомлення ---")
    print(f"🆔 Message ID: {message.message_id}")
    print(f"Чат: {message.chat.title or message.chat.id}")
    print(f"Дата: {message.date}")
    print(f"Текст: {content}")
    
    with open("channel_history.txt", "a", encoding="utf-8") as f:
        f.write(f"[{message.date}] ID: {message.message_id} | {content}\n")

async def main():
    print(f"Бот запущений! Слухаю канал {CHANNEL_ID}...")
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Бот зупинений.")
