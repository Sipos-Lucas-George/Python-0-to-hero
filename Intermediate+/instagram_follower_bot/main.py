"""
    Instagram Follower Bot, Follows Everybody From Another Account's Followers List
"""
import os
import dotenv

from instagram_follower_bot.bot import InstagramFollowerBot

dotenv.load_dotenv()

INSTAGRAM_USERNAME = os.getenv("INSTAGRAM_USERNAME")
INSTAGRAM_PASSWORD = os.getenv("INSTAGRAM_PASSWORD")
INSTAGRAM_ACCOUNT = os.getenv("INSTAGRAM_ACCOUNT")

bot = InstagramFollowerBot((INSTAGRAM_USERNAME, INSTAGRAM_PASSWORD), INSTAGRAM_ACCOUNT)
bot.login()
bot.find_followers()
bot.follow()
