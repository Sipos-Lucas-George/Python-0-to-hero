import os
import time

import dotenv

from instagram_not_follower_bot.bot import InstagramFollowerBot
from pyvirtualdisplay import Display

dotenv.load_dotenv()

INSTAGRAM_USERNAME = os.getenv("INSTAGRAM_USERNAME")
INSTAGRAM_PASSWORD = os.getenv("INSTAGRAM_PASSWORD")
INSTAGRAM_ACCOUNT = os.getenv("INSTAGRAM_ACCOUNT")

display1 = Display(visible=False, size=(1980, 1080))
display1.start()

bot1 = InstagramFollowerBot((INSTAGRAM_USERNAME, INSTAGRAM_PASSWORD), INSTAGRAM_ACCOUNT)
bot1.login()
bot1.find_followers()
bot1.save_followers()
display1.stop()
