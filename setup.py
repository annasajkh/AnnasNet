import os
import interactions
import asyncio

import clip_client
from docarray import DocumentArray
from utils import batching

bot = interactions.Client(token=os.environ["BOT_TOKEN"])

client = clip_client.Client("https://demo-cas.jina.ai:8443")

words_encoded = DocumentArray.load("src/words_encoded")