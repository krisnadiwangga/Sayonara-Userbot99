# 🍀 © @tofik_dn
# ⚠️ Do not remove credits


import random

from userbot import CMD_HELP
from userbot.events import register
from userbot import DEFAULTUSER
from telethon.tl.types import InputMessagesFilterVideo
from telethon.tl.types import InputMessagesFilterVoice
from telethon.tl.types import InputMessagesFilterPhotos


@register(outgoing=True, pattern=r"^\.meme$")
async def _(event):
    try:
        asupannya = [
            asupan
            async for asupan in event.client.iter_messages(
                "@VegetaVideoPack", filter=InputMessagesFilterVideo
            )
        ]
        kontol = await event.client.get_me()
        await event.client.send_file(
            event.chat_id,
            file=random.choice(asupannya),
            caption=f"Made by [{DEFAULTUSER}](tg://user?id={kontol.id})",
        )
        await event.delete()
    except Exception:
        await event.edit("Tidak bisa menemukan video asupan.")

CMD_HELP.update(
    {
        "asupan": "**Plugin : **`asupan`\
        \n\n  •  **Syntax :** `.meme`\
        \n  •  **Function : **Untuk Mengirim video memes secara random.\
    "
    }
)
