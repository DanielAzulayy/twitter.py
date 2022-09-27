import os
from typing import Dict

import tweepy
from dotenv import load_dotenv
from loguru import logger

load_dotenv()


class TweepyWrapper:
    __slots__ = "__credentials"

    def __init__(self):
        self.__credentials = self._load_credentials()

    def _load_credentials(self) -> Dict[str, str]:
        return {
            "consumer_key": os.getenv("CONSUMER_KEY", None),
            "consumer_secret": os.getenv("CONSUMER_SECRET", None),
            "access_token": os.getenv("ACCESS_TOKEN", None),
            "access_token_secret": os.getenv("ACCESS_TOKEN_SECRET", None),
        }

    def create_bot(self):
        try:
            auth = tweepy.OAuth1UserHandler(
                self.__credentials["consumer_key"],
                self.__credentials["consumer_secret"],
                self.__credentials["access_token"],
                self.__credentials["access_token_secret"],
            )
            return self._auth_bot(tweepy.API(auth))
        except Exception as e:
            logger.exception(e)

    def _auth_bot(self, api):
        """Authenticate the bot by the given API keys."""
        try:
            api.verify_credentials()
            logger.success("Bot authenticated successfully.")
            return api
        except Exception:
            logger.exception("Bot failed to authenticate.")
