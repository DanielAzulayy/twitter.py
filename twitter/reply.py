from loguru import logger

from twitter.tweepy_wrapper import TweepyWrapper
from utils.execute_code import execute_python


class ReplyBot:
    def __init__(self):
        self.twitter_api = TweepyWrapper().create_bot()

    def responder(self):
        mentions = self.twitter_api.mentions_timeline(count=1)
        for mention in mentions:
            if reply_text := self._get_reply_text(mention):
                self.twitter_api.update_status(
                    status=reply_text, in_reply_to_status_id=mention.id
                )

    def _get_reply_text(self, mention) -> str:
        try:
            self.twitter_api.create_favorite(mention.id)
            user_name = mention.user.screen_name
            code_output = str(execute_python(mention.text))
            return f"@{user_name} Code output:\n\n {code_output}"
        except SyntaxError as e:
            logger.info(f"User {user_name} sent invalid Python code.")
            return f"@{user_name} Make sure you send me valid Python code!\n Error: {e}"
        except Exception as e:
            logger.info(f"Tweet already replied or mentions not found {e}")
            return None
