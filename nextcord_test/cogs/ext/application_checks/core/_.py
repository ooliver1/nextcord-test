from __future__ import annotations

from typing import TYPE_CHECKING

from nextcord.ext.commands import Context

from .._ import application_checks

if TYPE_CHECKING:
    from nextcord_test.__main__ import MyBot


@application_checks.group()
async def core(ctx: Context):
    ...


def setup(bot: MyBot):
    ...
