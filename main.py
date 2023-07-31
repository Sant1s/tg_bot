import logging

from aiogram import executor
from aiogram.types import BotCommand

import bot
from bot import dp
import handlers.handlers
import handlers.states
import database

logging.basicConfig(level=logging.INFO)


async def setup_bot_commands():
    bot_commands = [
        BotCommand(command="/start", description="Start bot"),
        BotCommand(command="/commands", description="Get bot commands"),
        BotCommand(command="/tasks", description="Get all tasks"),
        BotCommand(command="/new_task", description="Add new task"),
        BotCommand(command="/done", description="Make task done")
    ]
    await bot.bot.set_my_commands(bot_commands)


async def on_startup(_):
    await database.db_start()
    await setup_bot_commands()


if __name__ == '__main__':
    print('Бот в онлайне!')
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
