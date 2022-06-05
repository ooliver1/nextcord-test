from __future__ import annotations

from typing import TYPE_CHECKING

from nextcord.ext.commands import Context

from .._ import cmdname

if TYPE_CHECKING:
    from nextcord_test.__main__ import MyBot


@cmdname.group()
async def cmdname2(ctx: Context):
    ...


def setup(bot: MyBot):
    ...
