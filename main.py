import asyncio
import logging
import sys
from aiogram import Bot, Dispatcher
from config import BOT_TOKEN
from handlers import base, admin, user
from middlewares import BanMiddleware



async def main():
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()

    # Register middleware
    dp.message.middleware(BanMiddleware())
    dp.callback_query.middleware(BanMiddleware())

    # Register routers
    dp.include_router(base.router)
    dp.include_router(admin.router)
    dp.include_router(user.router)

    logging.info("Starting bot...")
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        pass
