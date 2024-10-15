from asgiref.sync import sync_to_async

from phonenumbers import parse, is_valid_number_for_region
from phonenumbers.phonenumberutil import NumberParseException
from django.utils.translation import gettext as _
from django.contrib.auth import get_user_model
import uuid

User = get_user_model()


async def validate_phone_number(phone_number):
    try:
        parsed_number = parse(str(phone_number), 'UZ')
        if not is_valid_number_for_region(parsed_number, 'UZ'):
            return _("Kiritlgan telefon raqam faqat O'zbekiston hududiga tegishli bo'lishi kerak")

    except NumberParseException:
        return _("Noto'g'ri telefon raqam")

    try:
        user_exists = await sync_to_async(User.objects.get)(phone_number=phone_number)
        return _("Bunday foydalanuvchi mavjud")
    except User.DoesNotExist:
        return 'success'


async def create_user(**kwargs):
    try:
        password = kwargs.pop('password')
        user = User(**kwargs)
        user.set_password(password)
        await sync_to_async(user.save)()
    except:
        return 'error'


def generate_username():
    unique_id = str(uuid.uuid4())
    username = unique_id.replace('-', '')[:6]
    return username


