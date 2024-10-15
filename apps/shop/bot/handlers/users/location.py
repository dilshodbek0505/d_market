from apps.shop.bot.loader import dp
from geopy.distance import distance

from aiogram import F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext


store_coords = (41.2535592,69.2304708)

@dp.message(F.location)
async def get_location(msg: Message, state: FSMContext):
    location = msg.location
    
    user_coords = (location.latitude, location.longitude)

    dist_km = distance(store_coords, user_coords).km
    
    print(dist_km)

    
   