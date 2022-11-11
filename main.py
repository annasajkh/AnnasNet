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

try:
  bot.run(os.environ["BOT_TOKEN"])
except discord.errors.HTTPException:
  print("\n\n\nBLOCKED BY RATE LIMITS\nRESTARTING NOW\n\n\n")
  system("python restart.py")
  system("kill 1")