from bot.handlers.result_ai import result_router
from config.config import bot_config, BotConfig
import asyncio
from aiogram import Bot, Dispatcher
from keyboard.set_menu import set_main_menu
from handlers.user_handler import router, database
from handlers.quiz import router_quiz
from aiogram.fsm.storage.redis import RedisStorage, Redis


async def main() -> [bool | None]:
    """Main configuration function for create and start Bot"""
    if not database.connect:
        return False

    config: BotConfig = bot_config()

    bot = Bot(config.token, parse_mode='HTML')

    redis = Redis(host='localhost', db=0)
    storage = RedisStorage(redis=redis)

    dp = Dispatcher(storage=storage)

    await set_main_menu(bot)

    dp.include_routers(
        router,
        router_quiz,
        result_router
    )

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
