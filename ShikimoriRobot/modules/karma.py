import asyncio
import re

from pyrogram import filters

from ShikimoriRobot import BOT_USERNAME
from ShikimoriRobot import pbot as app
from ShikimoriRobot.modules.mongo.karma_mongo import (
    alpha_to_int,
    get_karma,
    get_karmas,
    int_to_alpha,
    is_karma_on,
    karma_off,
    karma_on,
    update_karma,
)
from ShikimoriRobot.utils.errors import capture_err
from random import choice
from ShikimoriRobot.utils.permission import adminsOnly

karma_positive_group = 3
karma_negative_group = 4

regex_upvote = r"^((?i)\+|\+\+|\+1|👍|pro|thanks|ty|great|good|noice|sexy|op)$"
regex_downvote = r"^(\-|\-\-|\-1|👎|noob|nub|bad|fu|chutiya|bkl)$"


KARMARANDOM = (
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
)

#moezilla add random point karma

@app.on_message(
    filters.text
    & filters.group
    & filters.incoming
    & filters.reply
    & filters.regex(regex_upvote, re.IGNORECASE)
    & ~filters.via_bot
    & ~filters.bot
    & ~filters.edited,
    group=karma_positive_group,
)
@capture_err
async def upvote(_, message):
    if not await is_karma_on(message.chat.id):
        return
    if not message.reply_to_message.from_user:
        return
    if not message.from_user:
        return
    if message.reply_to_message.from_user.id == message.from_user.id:
        return
    chat_id = message.chat.id
    user_id = message.reply_to_message.from_user.id
    user_mention = message.reply_to_message.from_user.mention
    current_karma = await get_karma(chat_id, await int_to_alpha(user_id))
    kip = choice(KARMARANDOM)
    if current_karma:
        current_karma = current_karma["karma"]
        karma = current_karma + int(kip)
    else:
        karma = 1
    new_karma = {"karma": karma}
    await update_karma(chat_id, await int_to_alpha(user_id), new_karma)
    await message.reply_text(
        f"Incremented Karma of {user_mention} By {kip}"
    )


@app.on_message(
    filters.text
    & filters.group
    & filters.incoming
    & filters.reply
    & filters.regex(regex_downvote, re.IGNORECASE)
    & ~filters.via_bot
    & ~filters.bot
    & ~filters.edited,
    group=karma_negative_group,
)
@capture_err
async def downvote(_, message):
    if not await is_karma_on(message.chat.id):
        return
    if not message.reply_to_message.from_user:
        return
    if not message.from_user:
        return
    if message.reply_to_message.from_user.id == message.from_user.id:
        return

    chat_id = message.chat.id
    user_id = message.reply_to_message.from_user.id
    user_mention = message.reply_to_message.from_user.mention
    current_karma = await get_karma(chat_id, await int_to_alpha(user_id))
    kdp = choice(KARMARANDOM)
    if current_karma:
        current_karma = current_karma["karma"]
        karma = current_karma - int(kdp)
    else:
        karma = 1
    new_karma = {"karma": karma}
    await update_karma(chat_id, await int_to_alpha(user_id), new_karma)
    await message.reply_text(
        f"Decremented Karma Of {user_mention} By {kdp}"
    )


# dear moezilla 😐 make karma personal stats code 

@app.on_message(filters.command("mykarma") & filters.group)
async def mykarma(_, message):   
    chat_id = message.chat.id
    user_id = message.from_user.id
    user_mention = message.from_user.mention
    current_karma = await get_karma(chat_id, await int_to_alpha(user_id))
    if current_karma:
        current_karma = current_karma["karma"]
        karma = current_karma 
        await message.reply_text(f"Your Total Point :- {karma}")



@app.on_message(filters.command("karmalist", f"karma@{BOT_USERNAME}") & filters.group)
@capture_err
async def command_karma(_, message):
    chat_id = message.chat.id
    if not message.reply_to_message:
        m = await message.reply_text("Getting Karma list of top 10 users wait...")
        karma = await get_karmas(chat_id)
        if not karma:
            await m.edit("No karma in DB for this chat.")
            return
        msg = f"🏆 Top list of Karma owners in the {message.chat.title}»: \n"
        limit = 0
        karma_dicc = {}
        for i in karma:
            user_id = await alpha_to_int(i)
            user_karma = karma[i]["karma"]
            karma_dicc[str(user_id)] = user_karma
            karma_arranged = dict(
                sorted(
                    karma_dicc.items(),
                    key=lambda item: item[1],
                    reverse=True,
                )
            )
        if not karma_dicc:
            await m.edit("No karma in DB for this chat.")
            return
        for user_idd, karma_count in karma_arranged.items():
            if limit > 9:
                break
            try:
                user = await app.get_users(int(user_idd))
                await asyncio.sleep(0.8)
            except Exception:
                continue
            first_name = user.first_name
            if not first_name:
                continue
            username = user.username
            msg += f"\n[{first_name}](https://t.me/{username}) — {karma_count}"
            limit += 1
        await m.edit(msg, disable_web_page_preview=True)
    else:
        user_id = message.reply_to_message.from_user.id
        karma = await get_karma(chat_id, await int_to_alpha(user_id))
        karma = karma["karma"] if karma else 0
        await message.reply_text(f"**Total Points**: __{karma}__")


# karma new toggle code made by @moezilla
@app.on_message(filters.command("karma") & ~filters.private)
@adminsOnly("can_change_info")
async def captcha_state(_, message):
    if not await is_karma_on(message.chat.id):
        await karma_on(message.chat.id)
        await bot.send_message(message.chat.id, f"""Karma Enable""")
    else:
        await karma_off(message.chat.id)
        await bot.send_message(message.chat.id, f"""Karma Disable""")



__mod_name__ = "Kᴀʀᴍᴀ"
__help__ = """

*Upvote* - Use upvote keywords like "+", "+1", "thanks", etc. to upvote a message.
*Downvote* - Use downvote keywords like "-", "-1", etc. to downvote a message.

*Commands*
 |• `/karma`:- reply to a user to check that user's karma points.
 |• `/mykarma`:- check your karma
 |• `/karmalist`:- send without replying to any message to check karma point list of top 10
 |• `/karma`:- Enable/Disable karma in your group.
"""
