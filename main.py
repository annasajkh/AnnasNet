from commands import *

from flask import Flask
from threading import Thread
from waitress import serve

app = Flask(__name__)


@app.route("/")
def main():
  return "your bot is alive"


def run():
  serve(app, host="0.0.0.0", port=8080)


def keep_alive():
  server = Thread(target=run)
  server.start()


keep_alive()


bot.run(os.environ["BOT_TOKEN"])