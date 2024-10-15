import asyncio, logging, sys

from django.core.management.base import BaseCommand
from django.conf import settings

from apps.shop.bot.loader import dp, bot
from apps.shop.bot.handlers import *


logging.basicConfig(level=logging.INFO)


class Command(BaseCommand):
    help = "Telegram bot"

    def handle(self, *args, **kwargs):
        
        async def main():
            await dp.start_polling(bot)
        
        logging.basicConfig(level=logging.INFO, stream=sys.stdout)
        asyncio.run(main())
