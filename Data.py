from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = """
Halo {}

Welcome to {}

Bot to create string telegram , 
1) pyrogram
2) telethon

This bot works to make it easier to get a string session via bot.
By @Stringsessessontelegrambot
    """

    # Home Button
    home_buttons = [
        [InlineKeyboardButton("🆕 Start​", callback_data="generate")],
        [InlineKeyboardButton(text="⚙️ Home​", callback_data="home")]
    ]

    generate_button = [
        [InlineKeyboardButton("Start Generate Session", callback_data="generate")]
    ]

    # Rest Buttons
    buttons = [
        [InlineKeyboardButton("Start Generate Session", callback_data="generate")],
        [InlineKeyboardButton("Maintaned By ​", url="https://t.me/telegram")],
        [
            InlineKeyboardButton("How To Use Me​​", callback_data="help"),
            InlineKeyboardButton("About Me​", callback_data="about")
        ],
        [InlineKeyboardButton("Info Other Bot​", url="https://t.me/AppleBotz")],
    ]

    # Help Message
    HELP = """
✨ **Available Commands** ✨

/about - Tentang Bot ini
/help - This Message
/start - Mulai Bot
/generate - Mulai Generating Session
/cancel - Membatalkan process
/restart - Membatalkan process
"""

    # About Message
    ABOUT = """
**About This Bot** 

Sebuah telegram bot untuk mengambil pyrogram dan telethon string session by @Stringsessiontelegrambot

Group Support : [Gabung](https://t.me/Telegram)
Framework : [Pyrogram](docs.pyrogram.org)
Language : [Python](www.python.org)
Developer : @Telegram
    """
