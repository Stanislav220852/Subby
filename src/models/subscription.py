from src.db.database import Base
import uuid
from datetime import datetime
from typing import List, TYPE_CHECKING
from sqlalchemy import String, DateTime, func
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey,String,NUMERIC,BigInteger

class Subscription(Base):
    __tablename__ = "subscriptions"

    id:Mapped[uuid.UUID] = mapped_column(primary_key=True,default=uuid.uuid4)
    user_id: Mapped[int] = mapped_column(BigInteger, ForeignKey("users.user_id"),ondelete = "CASCADE")
    title:Mapped[str] = mapped_column(String(255),unique=False,nullable=False)
    amount:Mapped[float] = mapped_column(NUMERIC(),unique=False,nullable=False)
    next_payment:Mapped[datetime] = mapped_column(DateTime(timezone=True),server_default=func.now())

    user: Mapped["User"] = relationship(back_populates="subscriptions")