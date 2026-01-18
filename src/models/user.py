from src.db.database import Base
import uuid
from datetime import datetime
from typing import List, TYPE_CHECKING
from sqlalchemy import String, DateTime, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

class User():
    __tablename__ = "users"

    id:Mapped[uuid.UUID] = mapped_column(primary_key=True,default=uuid.uuid4)
    user_id:Mapped[uuid.UUID] =  mapped_column(unique=True,nullable=False)
    username: Mapped[str] = mapped_column(String(50),unique=True,nullable=False)
    reated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())

