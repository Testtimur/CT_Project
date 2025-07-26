from aiogram.types import (ReplyKeyboardMarkup,KeyboardButton,
                           InlineKeyboardButton,InlineKeyboardMarkup)
from app.database.requests import get_categories

main = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="Каталог")],
                           [KeyboardButton(text="Корзина")],
                           [KeyboardButton(text="Контакты")],
                           [KeyboardButton(text="О нас")]],
                           resize_keyboard=True,
                           input_field_placeholder="Выберете пункт меню")

async def category():
    all_categories = await get_categories()


get_number = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="Отправить номер",
                                                           request_contact=True)]],
                                 resize_keyboard=True)
