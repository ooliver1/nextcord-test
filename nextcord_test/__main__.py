from __future__ import annotations

from asyncio import set_event_loop_policy
from os import getenv

from botbase import BotBase
from dotenv import load_dotenv
from nextcord import Intents
from uvloop import EventLoopPolicy

set_event_loop_policy(EventLoopPolicy())
load_dotenv()


class MyBot(BotBase):
    ...


intents = Intents.all()
bot = MyBot(intents=intents)


bot.run(getenv("TOKEN"))
