# Thanks Full To Team Ultroid
# Ported By Vcky @VckyouuBitch + @MaafGausahSokap
# Copyright (c) 2021 Geez - Projects
# Geez - Projects https://github.com/Vckyou/Geez-UserBot
# VEGETA-USERBOT https://github.com/Randi356/VEGETA-USERBOT
# Ini Belum Ke Fix Ya Bg :')
# Ambil aja gapapa tp Gaguna kaya hidup lu Woakkakaka


from telethon.tl.functions.channels import GetFullChannelRequest as getchat
from telethon.tl.functions.phone import CreateGroupCallRequest as startvc
from telethon.tl.functions.phone import DiscardGroupCallRequest as stopvc
from telethon.tl.functions.phone import GetGroupCallRequest as getvc
from telethon.tl.functions.phone import InviteToGroupCallRequest as invitetovc

from telethon.tl.types import ChatAdminRights
from userbot import CMD_HELP
from userbot.events import register

NO_ADMIN = "`LU BUKAN ADMIN NGENTOT!!`"


async def get_call(event):
    vegetabot = await event.client(getchat(event.chat_id))
    ren = await event.client(getvc(vegetabot.full_chat.call))
    return ren.call


def user_list(l, n):
    for i in range(0, len(l), n):
        yield l[i: i + n]


@register(outgoing=True, pattern=r"^\.startvc$", groups_only=True)
async def _(vegetabot):
    chat = await vegetabot.get_chat()
    admin = chat.admin_rights
    creator = chat.creator

    if not admin and not creator:
        return await vegetabot.edit(NO_ADMIN)
    new_rights = ChatAdminRights(invite_users=True)
    try:
        await vegetabot.client(startvc(vegetabot.chat_id))
        await vegetabot.edit("`OBROLAN SUARA DIMULAI, YANG ONCAM LO NGENTOT...`")
    except Exception as ex:
        await vegetabot.edit(f"`{str(ex)}`")


@register(outgoing=True, pattern=r"^\.stopvc$", groups_only=True)
async def _(vegetabot):
    chat = await vegetabot.get_chat()
    admin = chat.admin_rights
    creator = chat.creator

    if not admin and not creator:
        return await vegetabot.edit(NO_ADMIN)
    new_rights = ChatAdminRights(invite_users=True)
    try:
        await vegetabot.client(stopvc(await get_call(vegetabot)))
        await vegetabot.edit("`OBROLAN SUARA DIHENTIKAN, TYPING AJAYA NGENTOT...`")
    except Exception as ex:
        await vegetabot.edit(f"`{str(ex)}`")


@register(outgoing=True, pattern=r"^\.vcinvite", groups_only=True)
async def _(vegetaot):
    await vegetabot.edit("`Memulai Invite member group...`")
    users = []
    z = 0
    async for x in vegetabot.client.iter_participants(vegetabot.chat_id):
        if not x.bot:
            users.append(x.id)
    hmm = list(user_list(users, 6))
    for p in hmm:
        try:
            await vegetabot.client(invitetovc(call=await get_call(vegetabot), users=p))
            z += 6
        except BaseException:
            pass
    await vegetabot.edit(f"`Menginvite {z} Member`")


CMD_HELP.update(
    {
        "vegetacalls": "𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.startvc`\
         \n↳ : Memulai Obrolan Suara dalam Group.\
         \n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.stopvc`\
         \n↳ : `Menghentikan Obrolan Suara Pada Group.`\
         \n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.vcinvite`\
         \n↳ : Invite semua member yang berada di group. (Kadang bisa kadang kaga)."
    }
)
