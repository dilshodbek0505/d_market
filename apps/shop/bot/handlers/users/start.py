from asgiref.sync import sync_to_async

from aiogram.filters import CommandStart
from aiogram.types import Message

from apps.shop.bot.loader import dp
from apps.shop.bot.keyboards.default import keyboard

from django.contrib.auth import get_user_model

User = get_user_model()


@dp.message(CommandStart())
async def start_command(msg: Message):
    telegram_id = msg.from_user.id
    try:
        user = await sync_to_async(User.objects.get)(telegram_id = telegram_id)
        await msg.answer(f'Xush kelibsiz {user.username}', reply_markup=keyboard.main_kb())
    except User.DoesNotExist:
        await msg.answer('Foydalanuvchi topilmadi', reply_markup=keyboard.register_kb())
    

