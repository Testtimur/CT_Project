from app.database.models import async_session
from app.database.models import User,Item,Category
from sqlalchemy import select

async def set_user(tg_id):
    async with async_session() as session:
        user = await session.scalar(select(User).where(User.tg_id == tg_id))