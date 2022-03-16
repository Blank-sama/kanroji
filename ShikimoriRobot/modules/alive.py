import asyncio
import telegram
import os
import requests
import datetime
import time
from PIL import Image
from io import BytesIO
from datetime import datetime
import random
from telethon import events, Button, custom, version
from ShikimoriRobot.events import register
from ShikimoriRobot import telethn as borg, OWNER_ID
from ShikimoriRobot import StartTime, dispatcher
from telethon.tl.types import ChannelParticipantsAdmins
from pyrogram import __version__ as pyro


edit_time = 5
""" =======================CONSTANTS====================== """
file1 = "https://telegra.ph//file/38d71dde31b5f10b04d77.jpg"
file2 = "https://telegra.ph//file/ad7c7ccdd4db3795f0d50.jpg"
file3 = "https://telegra.ph//file/62a5a4b9bf563caac526b.jpg"
file4 = "https://telegra.ph//file/bead833fe37b0dc1f42d4.jpg"
file5 = "https://telegra.ph//file/ac577854aeb7b21d6bbc7.jpg"
file6 = "https://telegra.ph//file/b0e0068dc409ae71171d2.jpg"
""" =======================CONSTANTS====================== """

START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ('week', 60 * 60 * 24 * 7),
    ('day', 60 * 60 * 24),
    ('hour', 60 * 60),
    ('min', 60),
    ('sec', 1)
)

async def _human_time_duration(seconds):
    if seconds == 0:
        return 'inf'
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append('{} {}{}'
                         .format(amount, unit, "" if amount == 1 else "s"))
    return ', '.join(parts)

@register(pattern=("/alive"))
async def hmm(yes):
    chat = await yes.get_chat()
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    Shu = f"♡ **Hey [{yes.sender.first_name}](tg://user?id={yes.sender.id}), I'm Shikimori**\n"
    Shu += f"♡ **My Uptime** ~♪ `{uptime}`\n"
    Shu += f"♡ **Telethon Version** ~♪ `{version.__version__}`\n"
    Shu += f"♡ **Python Telegram Bot Version** ~♪ `{telegram.__version__}`\n"
    Shu += f"♡ **Pyrogram Version** ~♪ `{pyro}`\n"
    Shu += f"♡ **My Darling** ~♪ [Sawada Tsunayoshi](tg://user?id={OWNER_ID})"
    BUTTON = [[Button.url("ʜᴇʟᴘ", f"https://t.me/Shikimori_Robot?start=help"),Button.url("sᴜᴘᴘᴏʀᴛ", f"https://t.me/NobaraSupport"),],[Button.url("♡ᴅᴀʀʟɪɴɢ♡", f"https://t.me/Sawada_Kun")]]
    on = await borg.send_file(yes.chat_id, file=file2,caption=Shu, buttons=BUTTON)

    await asyncio.sleep(edit_time)
    ok = await borg.edit_message(yes.chat_id, on, file=file6, buttons=BUTTON) 

    await asyncio.sleep(edit_time)
    ok2 = await borg.edit_message(yes.chat_id, ok, file=file5, buttons=BUTTON)

    await asyncio.sleep(edit_time)
    ok3 = await borg.edit_message(yes.chat_id, ok2, file=file4, buttons=BUTTON)
    
    await asyncio.sleep(edit_time)
    ok4 = await borg.edit_message(yes.chat_id, ok3, file=file3, buttons=BUTTON)
    
    await asyncio.sleep(edit_time)
    ok5 = await borg.edit_message(yes.chat_id, ok4, file=file2, buttons=BUTTON)
    
    await asyncio.sleep(edit_time)
    ok6 = await borg.edit_message(yes.chat_id, ok5, file=file1, buttons=BUTTON)
    
