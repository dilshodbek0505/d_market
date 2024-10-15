from aiogram.types import ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from django.utils.translation import gettext as _

def register_kb() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardBuilder()
    kb.button(text=_('Register'))
    kb.adjust(2)
    return kb.as_markup(resize_keyboard=True)

def contact_kb() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardBuilder()
    kb.button(text=_('Telfon raqam'), request_contact=True)
    return kb.as_markup(resize_keyboard=True)

def main_kb() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardBuilder()
    kb.button(text=_("Manzilni aniqlash"), request_location=True)
    return kb.as_markup(resize_keyboard=True)