# ← NEW FILE: api/models.py

from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float, DateTime

class Base(DeclarativeBase):
    pass

class Dive(Base):
    __tablename__ = "dives"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    location: Mapped[str] = mapped_column(String)
    site: Mapped[str] = mapped_column(String)
    max_depth: Mapped[float] = mapped_column(Float)
    date: Mapped[DateTime] = mapped_column(DateTime)
