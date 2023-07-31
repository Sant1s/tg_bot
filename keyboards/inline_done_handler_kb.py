from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from bot import bot, dp


async def make_user_tasks_kb(tasks_list: list):
    inline_kb = InlineKeyboardMarkup()
    for item in tasks_list:
        inline_kb.add(InlineKeyboardButton("{}".format(item[1]), callback_data="{}".format(item[1])))
    return inline_kb
