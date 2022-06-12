from __future__ import annotations

from typing import TYPE_CHECKING

from botbase import CogBase
from nextcord import ClientCog, Interaction, slash_command
from nextcord.ext.application_checks import bot_has_any_role as app_bot_has_any_role
from nextcord.ext.commands import Context

from ._ import core

if TYPE_CHECKING:
    from nextcord_test.__main__ import MyBot


@core.group()
async def bot_has_any_role(ctx: Context):
    ...


@bot_has_any_role.command()
async def test(ctx: Context):
    await ctx.send("Run /test_bot_has_any_role")


class BotHasAnyRole(CogBase):
    @slash_command(description="Requires `test` or `test2` role")
    @app_bot_has_any_role("test", "test2")
    async def test_bot_has_any_role(self, inter: Interaction):
        await inter.send("You got lucky")

    @test_bot_has_any_role.error
    async def test_bot_has_any_role_err(
        self: ClientCog, inter: Interaction, exc: Exception
    ):
        await inter.send(f"Yay {exc}")


def setup(bot: MyBot):
    bot.add_cog(BotHasAnyRole(bot))
