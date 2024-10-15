from asgiref.sync import sync_to_async

from aiogram.types import Message
from aiogram import F
from aiogram.fsm.context import FSMContext

from apps.shop.bot.loader import dp
from apps.shop.bot.states.state import Register
from apps.shop.bot.keyboards.default.keyboard import contact_kb
from apps.user.utils import generate_code
from apps.shop.bot.handlers.users.utils import validate_phone_number, create_user, generate_username

from django.contrib.auth import get_user_model
from django.core.cache import cache
from django.utils.translation import gettext as _
from django.contrib.auth.hashers import make_password


User = get_user_model()



@dp.message(F.text == 'Register')
async def register_user(msg: Message, state: FSMContext):
    text = _("Yaxshi keling ro'yxatdan o'tamiz.\nTelfon raqamingizni jo'nating: (+998991116677)")
    
    await msg.answer(text, reply_markup=contact_kb())
    
    await state.set_state(Register.phone_number)



@dp.message(Register.phone_number, F.text)
async def get_phone_number_by_text(msg: Message, state: FSMContext):
    phone_number = msg.text
    validate = await validate_phone_number(phone_number)
    
    if validate != 'success':
        await msg.answer(validate)
    
    else:
    
        if cache.get(f'otp_{phone_number}'):
            print(cache.get(f'otp_{phone_number}'))
            await msg.answer(_('Kod yuborilgan!'))
        
        else:
            code = generate_code()
            cache.set(f'otp_{phone_number}', code, 60 * 2)
            print(code)

            await state.update_data({
                'phone_number': phone_number
            })
            
            await msg.answer(_("Tasdiqlash kodini kiriting: "))
            await state.set_state(Register.confirm_otp)


@dp.message(Register.phone_number, F.contact)
async def get_phone_number_by_contact(msg: Message, state: FSMContext):
    phone_number = msg.contact.phone_number
    
    validate = await validate_phone_number(phone_number)
    if validate != 'success':
        await msg.answer(validate)
    
    else:
        if cache.get(f'otp_{phone_number}'):
            await msg.answer(_('Kod yuborilgan!'))
        
        else:    
            code = generate_code()
            cache.set(f'otp_{phone_number}', code, 60 * 2)
            
            await state.update_data({
                'phone_number': phone_number
            })
            
            await msg.answer(_("Tasdiqlash kodini kiriting: "))
            await state.set_state(Register.confirm_otp)

    
    
@dp.message(Register.confirm_otp, F.text)
async def confirm_otp(msg: Message, state: FSMContext):
    data = await state.get_data()
    
    phone_number = data.get('phone_number')
    code = cache.get(f'otp_{phone_number}')
    confirm_code = msg.text
    
    if code != confirm_code:
        await msg.answer(_("Kod mos kelmadi!"))
    
    else:
        cache.delete(f'otp_{phone_number}')
        
        await msg.answer(_("Parol kiriting: "))
        await state.set_state(Register.password)


@dp.message(Register.password, F.text)
async def set_password(msg: Message, state: FSMContext):
    await state.update_data({
        'password': msg.text
    })
    
    await msg.answer(_("Parolni takrorlang: "))
    await state.set_state(Register.confirm_password)


@dp.message(Register.confirm_password, F.text)
async def set_confirm_password(msg: Message, state: FSMContext):
    data = await state.get_data()
    
    password = data.get('password')
    if password != msg.text:
        await msg.answer(_("Parol xato kiritlgan!"))
        
        await msg.answer(_("Parol kiriting: "))
        await state.set_state(Register.password)
    
    else:
        username = msg.from_user.username
        phone_number = data.get('phone_number')
        
        if not username:
            username = generate_username()
            
        user = await create_user(
            password = password,
            username = username,
            phone_number = phone_number,
            telegram_id = msg.from_user.id
        )
        
        if user == 'error':
            await msg.answer(_("Nimadir xato ketdi iltmos qayta urinig!"))
        else:
            await msg.answer(_("Muvoffaqiyatli bajarildi!"))
    
        await state.clear()
    
        
        