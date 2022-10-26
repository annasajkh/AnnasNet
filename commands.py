from setup import *


@bot.command(
  name="describe",
  description="describe an image using CLIP Model",
  options=[
    interactions.Option(
      name="image",
      description="image to describe",
      type=interactions.OptionType.ATTACHMENT,
      required=True,
    ),
  ],
)
async def describe(ctx: interactions.CommandContext,
                   image: interactions.Attachment) -> None:
  await ctx.defer()

  image_encoded = await client.aencode([image.url])
  result = ", ".join(words_encoded.find(query=image_encoded,limit=5)[0].texts).strip()

  embed = interactions.Embed(
    image=interactions.EmbedImageStruct(url=image.url),
    footer=interactions.EmbedFooter(text=result)
  )

  await ctx.send(embeds=embed)