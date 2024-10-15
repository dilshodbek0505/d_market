from aiogram.types import ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from django.utils.translation import gettext as _

def register_kb() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardBuilder()
    kb.button(text=_('Register'))
    kb.adjust(2)
    return kb.as_markup(resize_keyboard=True)