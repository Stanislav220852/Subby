from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from src.db.models import User







class UserServices:
    @staticmethod
    async def add_user(db: AsyncSession, user_id: int, username: str):
    
        query_user = select(User).where(User.user_id == user_id)
        result = await db.execute(query_user)
        if not user:
            new_user = User(id=user_id, username=username)
            db.add(new_user)
            await db.commit()
            await db.refresh(new_user)
            