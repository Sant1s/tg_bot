from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup


class NewTaskStates(StatesGroup):
    task_name = State()
    task_time = State()

