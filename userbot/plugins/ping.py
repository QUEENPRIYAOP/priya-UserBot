import asyncio
from datetime import datetime
import time

from .. import ALIVE_NAME, CMD_HELP
from ..utils import admin_cmd, edit_or_reply, sudo_cmd

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Crystal User"




@borg.on(admin_cmd(pattern="ping$"))
@borg.on(sudo_cmd(pattern="ping$", allow_sudo=True))
async def _(event):
    text = f"""
┏━━━┓━━━━━━━━━┓
┃┏━┓┃━━━━━━━━━┃
┃┗━┛┃━━┓━┓━━━┓┃
┃┏━━┛┏┓┃┏┓┓┏┓┃┛
┃┃━━━┗┛┃┃┃┃┗┛┃┓
┗┛━━━━━┛┛┗┛━┓┃┛
━━━━━━━━━━━━┛┃━
━━━━━━━━━━━━━┛━
__𝘿3𝙑𝙄𝙇 𝙋𝙍𝙄𝙔𝘼__ is **ON!**ツ
•My Master→ {DEFAULTUSER}
↓||•Ms•||↓
Support :- @Bustedmindss
"""
    st = time.time()

    await event.edit(text)

    et = time.time()
    text += f"\n`{round((et - st), 3)} ms`"

    await event.edit(text)


CMD_HELP.update(
    {
        "ping": "**Ping**\
\n\n**Syntax : **`.ping`\
\n**Usage :** Get speed of your bot."
    }
)

