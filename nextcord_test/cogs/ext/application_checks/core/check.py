from __future__ import annotations

from asyncio import sleep
from random import choice
from typing import TYPE_CHECKING

from botbase import CogBase
from nextcord import ClientCog, Interaction, slash_command
from nextcord.ext.application_checks import check as app_check
from nextcord.ext.commands import Context

from ._ import core

if TYPE_CHECKING:
    from nextcord_test.__main__ import MyBot


@core.group()
async def check(ctx: Context):
    ...


@check.command()
async def random(ctx: Context):
    await ctx.send("Run /random_test")


class Check(CogBase):
    @slash_command(description="Should not run")
    @app_check(lambda _: False)
    async def random_test(self, inter: Interaction):
        await inter.send("You got lucky")

    @random_test.error
    async def random_test_err(self: ClientCog, inter: Interaction, exc: Exception):
        await inter.send(f"Yay {exc}")


def setup(bot: MyBot):
    bot.add_cog(Check(bot))
