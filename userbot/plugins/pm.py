import asyncio
from userbot import *
from REBELBOT.utils import admin_cmd, edit_or_reply, sudo_cmd
from userbot.cmdhelp import CmdHelp
from userbot import ALIVE_NAME

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "REBEL"


@borg.on(admin_cmd(pattern="pm$"))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 3
    animation_ttl = range(0, 17)
    await event.edit("{first}")
    animation_chars = [
        "**ＳＵＮ♢**",
        "**ＰΞＲＳ♢ＮΛＬ░ＭΞＳＳΛＧΞ░ＫΛＲ♢**",
        f"**{DEFAULTUSER} ＰΞＲＳ♢ＮΛＬ ＭΞＳＳΛＧΞ ＫΛＲ♢**",    
    ]
    for i in animation_ttl:  # By @mafiarishabh for thanos bot

        await asyncio.sleep(animation_interval)
        await event.edit(
            animation_chars[i % 17], link_preview=True
        ) 
CmdHelp("personal message").add_command(
    'Pm', None, 'For personal massage'
).add()
