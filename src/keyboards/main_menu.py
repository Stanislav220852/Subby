from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def get_main_kb():
    kb = [
        [KeyboardButton(text="➕ Добавить подписку")],
        [KeyboardButton(text="📋 Мои подписки"), KeyboardButton(text="📊 Статистика")]
    ]
    return ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)