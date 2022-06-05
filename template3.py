from __future__ import annotations

from typing import TYPE_CHECKING

from botbase import CogBase
from nextcord.ext.commands import Context

from ._ import cmdname2

if TYPE_CHECKING:
    from nextcord_test.__main__ import MyBot


class FileName(CogBase):
    @cmdname2.group()
    async def cmdname3(self, ctx: Context):
        ...


def setup(bot: MyBot):
    bot.add_cog(FileName(bot))
