from __future__ import annotations

from typing import TYPE_CHECKING

from nextcord.ext.commands import Context, group

if TYPE_CHECKING:
    from nextcord_test.__main__ import MyBot


@group()
async def ext(ctx: Context):
    ...


def setup(bot: MyBot):
    bot.add_command(ext)
