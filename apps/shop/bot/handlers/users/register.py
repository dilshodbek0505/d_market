from asgiref.sync import sync_to_async

from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram import F
from aiogram.fsm.context import FSMContext

from apps.shop.bot.loader import dp
from apps.shop.bot.states import Register
from apps.user.utils import generate_code

from django.contrib.auth import get_user_model

User = get_user_model()


@dp.message(F.text == 'Register')
async def register_user(msg: Message, state: FSMContext):
    await msg.answer('Yaxshi keling ro\'yhatdan o\'tamiz.\nTelfon raqamingizni yuboring: +998991112233')
    await state.set_state(Register.phone_number.state)


@dp.message(Register.phone_number, F.text)
async def get_phone_number(msg: Message, state: FSMContext):
    phone_number = msg.text
    # phone number validate
    # sent sms code
    code = generate_code()
    print(code)
    await state.update_data({
        'code': code
    })
    await msg.answer('Tasdiqlash kodini kirting: ')
    await state.set_state(Register.confirm_otp.state)
    

@dp.message(Register.confirm_otp, F.text)
async def get_confirm_code(msg: Message, state: FSMContext):
    data = await state.get_data()
    code = data.get('code')
    confirm_code = msg.text
    
    if code != confirm_code:
        await msg.answer('Kod to\'g\'ri kelmadi')
    else:
        await msg.answer('Ro\'yxatdan o\'tdingiz')
    
    await state.clear()


@dp.message(F.text == 'Bosh menu')
async def main_menu(msg: Message, state: FSMContext):
    await msg.answer("Bosh menu")
    await state.clear()
    
    
    
    

