from fastapi import FastAPI, Request
from fastapi.responses import FileResponse
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from models import Base, User, Score
import greenlet


DATABASE_URL = "postgresql+asyncpg://karos:228@localhost/game_bot_db"

engine = create_async_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine, class_=AsyncSession)

app = FastAPI()

@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

@app.get("/")
async def root():
    return {"message": "Добро пожаловать в приложение!"}

@app.post("/submit_score")
async def submit_score(request: Request):
    data = await request.json()
    telegram_id = data.get('telegram_id')
    score = data.get('score')

    async with SessionLocal() as session:
        user = await session.get(User, telegram_id)
        if not user:
            user = User(telegram_id=telegram_id)
            session.add(user)
            await session.commit()
        new_score = Score(user_id=user.id, score=score)
        session.add(new_score)
        await session.commit()
    return {"status": "success"}
