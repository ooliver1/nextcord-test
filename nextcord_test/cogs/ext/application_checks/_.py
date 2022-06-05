from __future__ import annotations

from typing import TYPE_CHECKING

from nextcord.ext.commands import Context

from .._ import ext

if TYPE_CHECKING:
    from nextcord_test.__main__ import MyBot


@ext.group()
async def application_checks(ctx: Context):
    ...


def setup(bot: MyBot):
    ...
