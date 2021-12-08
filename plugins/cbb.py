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
            text = f"<b>✯ ᴄʀᴇᴀᴛᴏʀ : <a href='tg://user?id={OWNER_ID}'>✭ Iϻsαi🎭Arⱥ𝖘aภ ✭</a>\n✯ ʟᴀɴɢᴜᴀɢᴇ : <code>Python3</code>\n✯ ʟɪʙʀᴀʀʏ : <a href='https://docs.pyrogram.org/'>Pyrogram asyncio {__version__}</a>\n✯ ꜱᴏᴜʀᴄᴇ ᴄᴏᴅᴇ : <a href='https://github.com/imsaravanakrish'>ᴄʟɪᴄᴋ ʜᴇʀᴇ</a>\n✯ ᴜᴘᴅᴀᴛᴇꜱ ᴄʜᴀɴɴᴇʟ : @TamilBots\n✯ ꜱᴜᴘᴘᴏʀᴛ ɢʀᴏᴜᴘ : @TamilSupport</b>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("🔒 Close", callback_data = "close"),
                        InlineKeyboardButton("↞ Back", callback_data = "Back")
                    ]
                ]
            )
        )
       
    elif data == "Back":
        buttons = [[
            InlineKeyboardButton('ᴊᴏɪɴ ᴍʏ ᴍᴏᴠɪᴇ ɢʀᴏᴜᴘ', url=f'http://t.me/TamilMoviesChat')
            ],[
            InlineKeyboardButton('ꜱᴜᴘᴘᴏʀᴛ ᴄʜᴀᴛ', url='https://t.me/TamilSupport'),
            InlineKeyboardButton('🤖 Updates', url='https://t.me/TamilBots')
            ],[
            InlineKeyboardButton('😊 About Me', callback_data ='about'),
            InlineKeyboardButton('🔒 Close', callback_data ='close')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            caption=START_MSG.format(
                first = message.from_user.first_name,
                last = message.from_user.last_name,
                username = None if not message.from_user.username else '@' + message.from_user.username,
                mention = message.from_user.mention,
                id = message.from_user.id
            ),            
            reply_markup=reply_markup,
            parse_mode='html'
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass
