from aiogram import Router, types
from aiogram.filters import CommandStart
from sqlalchemy.ext.asyncio import AsyncSession
from src.db.requests import add_user
from src.keyboards.main_menu import get_main_kb

router = Router()

@router.message(CommandStart())
async def cmd_start(message: types.Message, db: AsyncSession):
    await add_user(session, message.from_user.id, message.from_user.username)
    await message.answer(
        f"Привет, {message.from_user.full_name}! Я помогу следить за подписками.",
        reply_markup=get_main_kb()
    )