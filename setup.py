import os
import nextcord
from nextcord.ext import commands

import clip_client
from docarray import DocumentArray

client = clip_client.Client("https://demo-cas.jina.ai:8443")

words_encoded = DocumentArray.load("src/words_encoded")

bot = commands.Bot()

@bot.event
async def on_ready():
  print(f"logged as {bot.user}")