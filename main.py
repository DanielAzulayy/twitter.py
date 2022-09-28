from flask import Flask
from twitter.reply import ReplyBot
from apscheduler.schedulers.background import BackgroundScheduler
import atexit

application = Flask(__name__)
bot = ReplyBot()


def run_bot():
    bot.responder()


scheduler = BackgroundScheduler()
scheduler.add_job(func=run_bot, trigger="interval", seconds=5)
scheduler.start()


@application.route("/")
def index():
    return "@danielazulayy"


atexit.register(lambda: scheduler.shutdown())

if __name__ == "__main__":
    application.run(port=8000)
