from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

start_button = KeyboardButton('/start')
commands_button = KeyboardButton('/commands')
tasks_button = KeyboardButton('/tasks')
new_tasks_button = KeyboardButton('/new_task')
done_button = KeyboardButton('/done')

client_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)

client_keyboard.row(start_button, commands_button).add(tasks_button).row(new_tasks_button, done_button)
