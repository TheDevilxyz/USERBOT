from RAUSHAN import app, API_ID, API_HASH
from config import ALIVE_PIC
from pyrogram import filters, Client
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message

START_TEXT = """
|────────────────────|
| ⚡ ʜᴇʏ, ɪ ᴀᴍ : {0}
| ⚙️ ᴀᴅᴠᴀɴᴄᴇᴅ ᴀɴɪᴍᴀᴛɪᴏɴ + ғᴜɴ ᴛᴏᴏʟs
| 🔐 ғᴀsᴛ • sᴇᴄᴜʀᴇ • ᴍᴏᴅᴜʟᴀʀ
|────────────────────|

| ʜᴏᴡ ᴛᴏ ᴜsᴇ ᴍᴇ: Click Tips
| ɢᴇɴᴇʀᴀᴛᴇ ꜱᴇꜱꜱɪᴏɴ: @AnanyaSessionBot
|────────────────────|
| ᴄʟᴏɴᴇ ʙᴏᴛ ɪɴ 2 sᴇᴄᴏɴᴅs:
| /clone session_string
| ʀᴇᴍᴏᴠᴇ ᴄʟᴏɴᴇ:
| /delclone session_string
| /logout session_string
|────────────────────|
| ᴘᴏᴡᴇʀᴇᴅ ʙʏ: ˹ ᴅᴇᴛᴏx ʙᴏᴛs ˼
|────────────────────|
"""

@app.on_message(filters.command("start"))
async def hello(client: Client, message: Message):
    bot = await client.get_me()
    buttons = [
        [
            InlineKeyboardButton("˹ ᴏᴡɴᴇʀ ˼", url="https://t.me/darkxryan"),
            InlineKeyboardButton("˹ ᴜᴘᴅᴀᴛᴇs ˼", url="https://t.me/darkdtox"),
        ],
        [
            InlineKeyboardButton("˹ sᴜᴘᴘᴏʀᴛ ˼", url="https://t.me/ryanmusicsupport"),
            InlineKeyboardButton("˹ ᴍᴜsɪᴄ ˼", url="https://t.me/shreyaxmusicbot"),
        ],
        [
            InlineKeyboardButton("˹ sᴛʀɪɴɢ ɢᴇɴᴇʀᴀᴛᴏʀ ˼", url="https://t.me/AnanyaSessionBot"),
        ],
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    await client.send_photo(
        message.chat.id,
        ALIVE_PIC,
        caption=START_TEXT.format(bot.mention),
        reply_markup=reply_markup
    )

# © By itzshukla Your motherfucker if uh Don't gives credits.
@app.on_message(filters.command("clone"))
async def clone(bot: app, msg: Message):
    chat = msg.chat
    text = await msg.reply("Usage:\n\n /clone session")
    cmd = msg.command
    phone = msg.command[1]
    try:
        await text.edit("ᴡᴀɪᴛ ʙᴀʙʏ ғᴇᴡ sᴇᴄᴏɴᴅs...💌")
                   # change this Directry according to ur repo
        client = Client(name="Melody", api_id=API_ID, api_hash=API_HASH, session_string=phone, plugins=dict(root="RAUSHAN/modules"))
        await client.start()
        user = await client.get_me()
        await msg.reply(f" ᴊᴀ ᴘᴇʟ ᴅᴇ sᴀʙᴋᴏ ᴀʙ ᴅᴇᴛᴏx ᴋᴏ ʙᴀᴀᴘ ʙᴏʟ ᴋᴇ ᴊᴀɴᴀ 🥵 {user.first_name} 💨.")
    except Exception as e:
        await msg.reply(f"ERROR: {str(e)}\nPress /start to Start again.")