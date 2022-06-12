from __future__ import annotations

from typing import TYPE_CHECKING

from botbase import CogBase
from nextcord import ClientCog, Interaction, slash_command
from nextcord.ext.application_checks import (
    bot_has_guild_permissions as app_bot_has_guild_permissions,
)
from nextcord.ext.commands import Context

from ._ import core

if TYPE_CHECKING:
    from nextcord_test.__main__ import MyBot


@core.group()
async def bot_has_guild_permissions(ctx: Context):
    ...


@bot_has_guild_permissions.command()
async def test(ctx: Context):
    await ctx.send("Run /test_bot_has_guild_permissions")


class BotHasGuildPermissions(CogBase):
    @slash_command(description="Requires `test` role or `test2`")
    @app_bot_has_guild_permissions(administrator=True)
    async def test_bot_has_guild_permissions(self, inter: Interaction):
        await inter.send("You got lucky")

    @test_bot_has_guild_permissions.error
    async def test_bot_has_guild_permissions_err(
        self: ClientCog, inter: Interaction, exc: Exception
    ):
        await inter.send(f"Yay {exc}")


def setup(bot: MyBot):
    bot.add_cog(BotHasGuildPermissions(bot))
