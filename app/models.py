from app.database import Model
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey, func
import enum
import datetime

class JornalModel(Model):
    __tablename__ = 'jornal'

    id_journal: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users_table.user_id", ondelete="CASCADE"))
    lesson: Mapped[str]
    title: Mapped[str]
    description: Mapped[str]
    status: Mapped[bool] = mapped_column(default=False)
    create_at: Mapped[datetime.datetime] = mapped_column(server_default=func.now())
    data_lesson: Mapped[datetime.date]

class UserModel(Model):
    __tablename__ = 'users_table'

    user_id: Mapped[int] = mapped_column(primary_key=True)
    user_name: Mapped[str]
    user_password: Mapped[str]



