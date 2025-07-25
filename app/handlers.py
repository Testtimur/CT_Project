from aiogram.filters import CommandStart, Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, callback_query, CallbackQuery
from aiogram import F, Router


import app.keboards as kb
from app.auth import Register

router = Router()

@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer("Добро пожаловать в магазин индийского чая PAPAS MASALA!", reply_markup=kb.main)


@router.message(Command('help'))
async def cmd_help(message: Message):
    await message.answer('Вы нажали на кнопку помощи')

@router.message(F.text == 'Каталог')
async def catalog(message: Message):
    await message.answer('Выбирите категорию товара', reply_markup=kb.catalog)

@router.callback_query(F.data == 't-shirt')
async def t_shirt(callback: CallbackQuery):
    await callback.answer('Вы выбрали категорию',show_alert=True)
    await callback.answer('Вы выбрали категорию футболок')

@router.message(Command('register'))
async def register(message: Message, state: FSMContext):
    await state.set_state(Register.name)
    await message.answer('Введите ваше имя')

@router.message(Register.name)
async def register_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(Register.age)
    await message.answer('Введите ваше возраст')

@router.message(Register.age)
async def register_age(message: Message, state: FSMContext):
    await state.update_data(age=message.text)
    await state.set_state(Register.number)
    await message.answer('Отправьте ваш номер телефона',reply_markup=kb.get_number)

@router.message(Register.number, F.contact)
async def register_number(message: Message, state: FSMContext):
    await state.update_data(number=message.contact.phone_number)
    data = await state.get_data()
    await message.answer(f'Ваше имя: {data["name"]}\nВаш возраст: {data["age"]}\nВаш Номер: {data["number"]}')
    await state.clear()