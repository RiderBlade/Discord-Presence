from pypresence import Presence
import asyncio
from time import time

client_id = "Айди клиента"
RPC = Presence(client_id)

btns = [
    {
        "label": "Заказать бота",
        "url": "https://discord.gg/EutDHJznRR",
    },

    {
        "label": "Купить курс",
        "url": "https://discord.gg/4SNyafqMk6",
    },

]

RPC.connect()

RPC.update(
    state = '70+ ботов уже написанных',
    details = "TG: https://t.me/Rider_Dev",
    start = time(),
    buttons = btns,
    large_image = 'prog',
    small_image = 'xd',
    large_text = 'код',
    small_text = 'крутой значок',
)

async def main():
    await asyncio.sleep(100000)

asyncio.run(main())
