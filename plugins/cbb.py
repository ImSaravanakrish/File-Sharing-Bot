#(©)Codexbotz

from pyrogram import __version__
from bot import Bot
from config import OWNER_ID,START_MSG
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from database.sql import add_user, query_msg, full_userbase
from helper_func import subscribed, encode, decode, get_messages


@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"╭────[🔅ᴍᴏᴠɪʟᴇꜱ ʀᴏʙᴏᴛ🔅]───⍟\n │\n ├<b>🤖 Bot Name : <a href='https://t.me/MoviesLinkRoBot'>MoviesLinkBot</a></b>\n │\n ├<b>📢 Channel : <a href='https://t.me/TamilBots'>TamilBots</a></b>\n │\n ├<b>👥 Support Chat : <a href='https://t.me/TamilSupport'>TamilSupport</a></b>\n │\n ├<b>💢 Source : <a href='https://github.com/imsaravanakrish'>Click Here</a></b>\n │\n ├<b>🌐 Server : <a href='https://heroku.com'>Heroku</a></b>\n │\n ├<b>📕 Library : <a href='https://github.com/pyrogram'>Pyrogram 1.2.8</a></b>\n │\n ├<b>㊙ Language: <a href='https://www.python.org'>Python 3.9.4</a></b>\n │\n ├<b>👨‍💻 Developer : <a href='https://t.me/SaravanaKrish'>✭ Iϻsαi🎭Arⱥ𝖘aภ ✭</a></b>\n │\n ├<b>🚸 Powered By : <a href='https://t.me/TamilBots'>TamilBotZ</a></b>\n │\n ╰──────[Thanks 😊]───⍟",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("🔒 ᴄʟᴏꜱᴇ", callback_data = "close"),
                        InlineKeyboardButton("↞ ʙᴀᴄᴋ", callback_data = "Back")
                    ]
                ]
            )
        )
       
    elif data == "Back":
        buttons = [[
            InlineKeyboardButton('⚜ ᴊᴏɪɴ ᴏᴜʀ ᴍᴏᴠɪᴇ ɢʀᴏᴜᴘ ⚜', url=f'http://t.me/TamilMoviesChat')
            ],[
            InlineKeyboardButton('🌟 ᴍᴀɪɴ ᴄʜᴀɴɴᴇʟ 🌟', url='https://t.me/TamilMovies4K'),
            InlineKeyboardButton('♻️ ʙᴀᴄᴋᴜᴘ ᴄʜᴀɴɴᴇʟ ♻️', url='https://t.me/TamilMovieChat')
            ],[
            InlineKeyboardButton('😊 ᴀʙᴏᴜᴛ ᴍᴇ', callback_data ='about'),
            InlineKeyboardButton('🔒 ᴄʟᴏꜱᴇ', callback_data ='close')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text = f"ɪ ᴄᴀɴ ꜱᴛᴏʀᴇ ᴘʀɪᴠᴀᴛᴇ ꜰɪʟᴇꜱ ɪɴ ꜱᴘᴇᴄɪꜰɪᴇᴅ ᴄʜᴀɴɴᴇʟ ᴀɴᴅ ᴏᴛʜᴇʀ ᴜꜱᴇʀꜱ ᴄᴀɴ ᴀᴄᴄᴇꜱꜱ ɪᴛ ꜰʀᴏᴍ ꜱᴘᴇᴄɪᴀʟ ʟɪɴᴋ\n\nᴍᴀɪɴ ᴄʜᴀɴɴᴇʟ » @TamilMovies4K\nᴍᴏᴠɪᴇ ʀᴇQᴜᴇꜱᴛ ɢʀᴏᴜᴘ » @TamilMoviesChat",
            reply_markup = reply_markup,
            disable_web_page_preview = True
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass
