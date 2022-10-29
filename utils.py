from urllib.parse import urlparse
import nextcord


def uri_validator(text: str) -> bool:
  try:
    result = urlparse(text)
    return all([result.scheme, result.netloc])
  except:
    return False


def construct_embed(text: str = None, image_url: str = None) -> nextcord.Embed:
  embed = nextcord.Embed()

  if image_url:
    embed.set_image(image_url)

  if text:
    embed.set_footer(text=text)
  
  embed.color = nextcord.Color.blue()

  return embed

def get_raw_key(user_key: str):
  return "".join(user_key.split(".")[1:])