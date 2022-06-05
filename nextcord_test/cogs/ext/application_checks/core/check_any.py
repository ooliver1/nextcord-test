from __future__ import annotations

from random import choice
from typing import TYPE_CHECKING

from botbase import CogBase
from nextcord import ClientCog, Interaction, slash_command
from nextcord.ext.application_checks import check
from nextcord.ext.application_checks import check_any as app_check_any
from nextcord.ext.commands import Context

from ._ import core

if TYPE_CHECKING:
    from nextcord_test.__main__ import MyBot


@core.group()
async def check_any(ctx: Context):
    ...


@check_any.command()
async def random(ctx: Context):
    await ctx.send("Run /random_any_test")


class CheckAny(CogBase):
    @slash_command(description="Should sometimes run")
    @app_check_any(check((lambda _: False)), check((lambda _: choice((True, False)))))
    async def random_any_test(self, inter: Interaction):
        await inter.send("You got lucky")

    @random_any_test.error
    async def random_any_test_err(self: ClientCog, inter: Interaction, exc: Exception):
        await inter.send(f"Yay {exc}")


def setup(bot: MyBot):
    bot.add_cog(CheckAny(bot))
