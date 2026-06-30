from fastapi import FastAPI

# ← NEW: Import DB + models
from api.db import engine
from api.models import Base

app = FastAPI()

@app.on_event("startup")
async def startup_event():
    # ← NEW: Create tables automatically on startup
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

@app.get("/health")
def health():
    return {"status": "ok"}
