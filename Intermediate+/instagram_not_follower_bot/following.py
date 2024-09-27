import os
import time

import dotenv

from instagram_not_follower_bot.bot import InstagramFollowerBot
from pyvirtualdisplay import Display

dotenv.load_dotenv()

INSTAGRAM_USERNAME = os.getenv("INSTAGRAM_USERNAME")
INSTAGRAM_PASSWORD = os.getenv("INSTAGRAM_PASSWORD")
INSTAGRAM_ACCOUNT = os.getenv("INSTAGRAM_ACCOUNT")

display2 = Display(visible=False, size=(1980, 1080))
display2.start()

bot2 = InstagramFollowerBot((INSTAGRAM_USERNAME, INSTAGRAM_PASSWORD), INSTAGRAM_ACCOUNT)
time.sleep(3)
bot2.login()
bot2.find_following()
bot2.save_following()

display2.stop()
