# ← NEW FILE: api/db.py

from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
import os

DATABASE_URL = os.getenv("DATABASE_URL")

# ← NEW: Async engine using asyncpg
engine = create_async_engine(
    DATABASE_URL,
    echo=True,  # optional: logs SQL queries
)

# ← NEW: Async session factory
AsyncSessionLocal = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
)

# ← NEW: Dependency for FastAPI routes
async def get_db():
    async with AsyncSessionLocal() as session:
        yield session
