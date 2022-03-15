import os
import re
from platform import python_version as kontol
from telethon import events, Button
from telegram import __version__ as telever
from telethon import __version__ as tlhver
from pyrogram import __version__ as pyrover
from AsunaRobot.events import register
from AsunaRobot import telethn as tbot
import AsunaRobot.modules.sql.users_sql as sql


PHOTO = "https://te.legra.ph/file/ec23777561fa6d797d72e.mp4"

@register(pattern=("/alive"))
async def awake(event):
  TEXT = f"**Hi [{event.sender.first_name}](tg://user?id={event.sender.id}), I'm shouko komi 『ZΞ℞Ø』.** \n\n"
  TEXT += f"**I'm Working Properly** \n\n"
  TEXT += f"**My Master : [Blank Sama](https://t.me/girls_lob)** \n\n"
  TEXT += f"**Library Version :** `{telever}` \n"
  TEXT += f"**Telethon Version :** `{tlhver}` \n"
  TEXT += f"**Pyrogram Version :** `{pyrover}`\n"
  TEXT += "**Thanks For Adding Me Here ❤️**"
  BUTTON = [[Button.url("Help", "https://t.me/komiXRobot?start=help"), Button.url("Support", "https://t.me/komixsupport"), Button.url("Update", "https://t.me/komiinfo")]]
  await tbot.send_file(event.chat_id, PHOTO, caption=TEXT,  buttons=BUTTON)
