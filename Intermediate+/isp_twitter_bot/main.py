"""
    Internet Speed Provider Twitter Complaint Bot
"""
import os
import dotenv

from isp_twitter_bot.bot import InternetSpeedTwitterBot

dotenv.load_dotenv()

PROMISE_DOWN = 300
PROMISE_UP = 300
PAY_DOWN = 500
PAY_UP = 500
TWITTER_EMAIL = os.getenv("TWITTER_EMAIL")
TWITTER_PASSWORD = os.getenv("TWITTER_PASSWORD")
TWITTER_USERNAME = os.getenv("TWITTER_USERNAME")

bot = InternetSpeedTwitterBot((TWITTER_EMAIL, TWITTER_PASSWORD, TWITTER_USERNAME), (PROMISE_DOWN, PROMISE_UP), (PAY_DOWN, PAY_UP))
bot.get_internet_speed()
bot.tweet_at_provider()
