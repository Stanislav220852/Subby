from aiogram.fsm.state import StatesGroup, State

class AddSub(StatesGroup):
    title = State()          # Ожидаем название
    amount = State()         # Ожидаем цену
    next_payment = State()   # Ожидаем дату платежа