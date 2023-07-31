import aiogram
from aiogram.types import Message
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
import asyncio
from handlers.states import NewTaskStates
import database

import bot
from bot import dp

from keyboards.start_kb import client_keyboard
from keyboards.inline_done_handler_kb import make_user_tasks_kb
import database


@dp.message_handler(commands='start')
async def send_welcome(message: Message):
    await message.answer('Привет, Я бот менеджер задач\n'
                         'Команды, которые я могу выполнить\n'
                         '\t/start - запуск бота\n'
                         '\t/commands - получить список команд\n'
                         '\t/tasks - получить список задач\n'
                         '\t/new_task - добавить задачу\n'
                         '\t/done - убрать задачу\n', reply_markup=client_keyboard)


@dp.message_handler(commands='commands')
async def send_commands(message: Message):
    await message.answer('Вот список команд:\n'
                         '\t/start - запуск бота\n'
                         '\t/commands - получить список команд\n'
                         '\t/tasks - получить список задач\n'
                         '\t/new_task - добавить задачу\n'
                         '\t/done - убрать задачу из списка задач\n')


@dp.message_handler(commands='tasks')
async def get_tasks(message: Message):
    tasks = await database.get_user_tasks(message.from_user.id)
    for items in tasks:
        await message.answer(f'{items[1]}, до {items[2]}')


@dp.message_handler(commands='new_task', state=None)
async def get_new_task(message: Message):
    await NewTaskStates.task_name.set()
    await message.answer("Что вы хотите сделать?")


@dp.message_handler(state=NewTaskStates.task_name)
async def get_new_task_name(message: Message, state: FSMContext):
    async with state.proxy() as data:
        data['t_name'] = message.text
    await NewTaskStates.next()
    await message.answer("Какой дедлайн?")


@dp.message_handler(state=NewTaskStates.task_time)
async def get_new_task_time(message: Message, state: FSMContext):
    async with state.proxy() as data:
        await database.add_task(data['t_name'], message.text, message.from_user.id)
    await message.answer('Отлично!\n Я запомнил задачу')
    await state.finish()


@dp.message_handler(commands=['done'])
async def process_command_1(message: Message):
    await message.answer("Нажми на задачу, которую надо удалить",
                         reply_markup=await make_user_tasks_kb(await database.get_user_tasks(message.from_user.id)))


@dp.callback_query_handler()
async def delete_task(message: aiogram.types.CallbackQuery):
    await database.delete_task(message.data, message.from_user.id)
    await message.answer("Задача успешно снята!")
