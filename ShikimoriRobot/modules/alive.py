import os
import re
import random
from platform import python_version as kontol
from telethon import events, Button
from telegram import __version__ as telever
from telethon import __version__ as tlhver
from pyrogram import __version__ as pyrover
from ShikimoriRobot.events import register
from ShikimoriRobot import telethn as tbot


PHOTO = (
      "https://telegra.ph/file/b8a440f1dbbc0c17dabdf.jpg"
      "https://telegra.ph/file/541980d45561114fabc95.jpg"
      "https://telegra.ph/file/2a3a55d541ef99ffb9a27.jpg"
      "https://telegra.ph/file/5f1f7fa3cce1a39a3c53e.jpg"
)

@register(pattern=("/alive"))
async def awake(event):
  TEXT = f"**Koninchiwa [{event.sender.first_name}](tg://user?id={event.sender.id}), I'm ᴍɪᴛsᴜʀɪ.** \n\n"
  TEXT += "♡ **I'm Working Properly** \n\n"
  TEXT += f"♡ **My Owners: [See](https://t.me/MitsuriXOwner)** \n\n"
  TEXT += f"♡ **Library Version :** `{telever}` \n\n"
  TEXT += f"♡ **Telethon Version :** `{tlhver}` \n\n"
  TEXT += f"♡ **Pyrogram Version :** `{pyrover}` \n\n"
  TEXT += "**Thanks For Adding Me Here ♡**"
  BUTTON = [[Button.url("Help", "https://t.me/Mitsurixbot?start=help"), Button.url("Support", "https://t.me/MitsuriXSupport")]]
  await tbot.send_file(event.chat_id, random.choice(PHOTO), caption=TEXT,  buttons=BUTTON)
