from __future__ import annotations

from typing import TYPE_CHECKING

from botbase import CogBase
from nextcord import ClientCog, Interaction, slash_command
from nextcord.ext.application_checks import has_permissions as app_has_permissions
from nextcord.ext.commands import Context

from ._ import core

if TYPE_CHECKING:
    from nextcord_test.__main__ import MyBot


@core.group()
async def has_permissions(ctx: Context):
    ...


@has_permissions.command()
async def test(ctx: Context):
    await ctx.send("Run /test_has_permissions")


class HasPermissions(CogBase):
    @slash_command(description="Requires `test` role or `test2`")
    @app_has_permissions(administrator=True)
    async def test_has_permissions(self, inter: Interaction):
        await inter.send("You got lucky")

    @test_has_permissions.error
    async def test_has_permissions_err(
        self: ClientCog, inter: Interaction, exc: Exception
    ):
        await inter.send(f"Yay {exc}")


def setup(bot: MyBot):
    bot.add_cog(HasPermissions(bot))
