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
            text = f"<b>┏━━━━━━━━━❥\n ┣ Cʀᴇᴀᴛᴇʀ -> <a href=https://t.me/SaravanaKrish>✭ Iϻsαi🎭Arⱥ𝖘aภ ✭</a>\n ┣ Uᴘᴅᴀᴛᴇꜱ -> @TamilBots\n ┣ 𝖲ᴜᴘᴘᴏʀᴛ -> @TamilSupport\n ┗━━━━━━━━━❥",
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
            InlineKeyboardButton('ᴊᴏɪɴ ᴏᴜʀ ᴍᴏᴠɪᴇ ɢʀᴏᴜᴘ', url=f'http://t.me/TamilMoviesChat')
            ],[
            InlineKeyboardButton('ꜱᴜᴘᴘᴏʀᴛ ᴄʜᴀᴛ', url='https://t.me/TamilSupport'),
            InlineKeyboardButton('🤖 ᴜᴘᴅᴀᴛᴇꜱ', url='https://t.me/TamilBots')
            ],[
            InlineKeyboardButton('😊 ᴀʙᴏᴜᴛ ᴍᴇ', callback_data ='about'),
            InlineKeyboardButton('🔒 ᴄʟᴏꜱᴇ', callback_data ='close')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            caption= f"ʜᴇʟʟᴏ {first}\n\nɪ ᴄᴀɴ ꜱᴛᴏʀᴇ ᴘʀɪᴠᴀᴛᴇ ꜰɪʟᴇꜱ ɪɴ ꜱᴘᴇᴄɪꜰɪᴇᴅ ᴄʜᴀɴɴᴇʟ ᴀɴᴅ ᴏᴛʜᴇʀ ᴜꜱᴇʀꜱ ᴄᴀɴ ᴀᴄᴄᴇꜱꜱ ɪᴛ ꜰʀᴏᴍ ꜱᴘᴇᴄɪᴀʟ ʟɪɴᴋ\n\nᴍᴀɪɴ ᴄʜᴀɴɴᴇʟ » @TamilMovies4K\nᴍᴏᴠɪᴇ ʀᴇQᴜᴇꜱᴛ ɢʀᴏᴜᴘ » @TamilMoviesChat",            
            reply_markup=reply_markup,
            disable_web_page_preview = True
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass
