from aiogram.fsm.state import State, StatesGroup


class Register(StatesGroup):
    phone_number = State()
    confirm_otp = State()
    
    