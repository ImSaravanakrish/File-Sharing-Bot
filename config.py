import re
import os
import logging
from logging.handlers import RotatingFileHandler
from os import environ
#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "")

#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", ""))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "")

#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", ""))

#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", ""))

#Database 
DB_URI = os.environ.get("DATABASE_URL", "")

#force sub channel id, if you want enable force sub
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "0"))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

#start message
START_MSG = os.environ.get("START_MESSAGE", "Hello {first}\n\nI can store private files in Specified Channel and other users can access it from special link.")
try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

PICS = (environ.get('PICS', 'https://telegra.ph/file/7e56d907542396289fee4.jpg https://telegra.ph/file/9aa8dd372f4739fe02d85.jpg https://telegra.ph/file/adffc5ce502f5578e2806.jpg https://telegra.ph/file/6937b60bc2617597b92fd.jpg https://telegra.ph/file/09a7abaab340143f9c7e7.jpg https://telegra.ph/file/5a82c4a59bd04d415af1c.jpg https://telegra.ph/file/323986d3bd9c4c1b3cb26.jpg https://telegra.ph/file/b8a82dcb89fb296f92ca0.jpg https://telegra.ph/file/31adab039a85ed88e22b0.jpg https://telegra.ph/file/c0e0f4c3ed53ac8438f34.jpg https://telegra.ph/file/eede835fb3c37e07c9cee.jpg https://telegra.ph/file/e17d2d068f71a9867d554.jpg https://telegra.ph/file/8fb1ae7d995e8735a7c25.jpg https://telegra.ph/file/8fed19586b4aa019ec215.jpg https://telegra.ph/file/8e6c923abd6139083e1de.jpg https://telegra.ph/file/0049d801d29e83d68b001.jpg')).split()

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "Hello {first}\n\n<b>You need to join in my Channel/Group to use me\n\nKindly Please join Channel</b>")

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

#Set true if you want Disable your Channel Posts Share button
if os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True':
    DISABLE_CHANNEL_BUTTON = True
else:
    DISABLE_CHANNEL_BUTTON = False

ADMINS.append(OWNER_ID)
ADMINS.append(1250450587)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
