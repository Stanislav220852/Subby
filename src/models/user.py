from src.db.database import Base
import uuid
from datetime import datetime
from typing import List, TYPE_CHECKING
from sqlalchemy import String, DateTime, func
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String,BigInteger

class User(Base):
    __tablename__ = "users"

    id:Mapped[uuid.UUID] = mapped_column(primary_key=True,default=uuid.uuid4)
    user_id:Mapped[int] =  mapped_column(BigInteger,unique=True,nullable=True)
    username: Mapped[str] = mapped_column(String(50),unique=True,nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())

    subscription = Mapped[List["Subscription"]] = relationship(
        back_populates="user", cascade="all, delete-orphan"
    )