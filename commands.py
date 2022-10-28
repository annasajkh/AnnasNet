from setup import *

@bot.slash_command(
  name="describe",
  description="describe an image using CLIP Model",
)
async def describe(interaction: nextcord.Interaction, image: nextcord.Attachment = nextcord.SlashOption(required=True)) -> None:
  await interaction.response.defer()
  
  image_encoded = await client.aencode([image.url])
  
  result = ", ".join(words_encoded.find(query=image_encoded, limit=5)[0].texts).strip()

  embed = nextcord.Embed()
  embed.set_image(image.url)
  embed.set_footer(text=result)
  
  await interaction.followup.send(embed=embed)

