#(©)Codexbotz

from pyrogram import __version__
from bot import Bot
from config import OWNER_ID,START_MSG
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from database.sql import add_user, query_msg, full_userbase
from helper_func import subscribed, encode, decode, get_messages
from script import Scripted


@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text=Scripted.START_TEXT,
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
            text=Scripted.NEW_TXT,
            reply_markup=reply_markup,
            disable_web_page_preview = True
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass
