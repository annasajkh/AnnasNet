from setup import *



@bot.slash_command(
  name="put",
  description="put item into the database".strip(),
)
async def put(interaction: nextcord.Interaction,
              key : str = nextcord.SlashOption(required=True,
                                               description="text that will be used to get the item"),
              attachment: nextcord.Attachment = nextcord.SlashOption(required=True,
                                                                     description="item to be put in")
):  
  await interaction.response.defer()

  try:
    print(db[key])
    await interaction.followup.send(f"\"{key}\" aready exist in the database please use different key")
    return
  except:
    pass
  
  db[key] = attachment.url
  
  await interaction.followup.send(f"successfully put \"{key}\" into the database")



@bot.slash_command(
  name="put_text",
  description="put text item into the database".strip(),
)
async def put_text(interaction: nextcord.Interaction,
              key : str = nextcord.SlashOption(required=True,
                                               description="text that will be used to get the item"),
              text : str = nextcord.SlashOption(required=True,
                                                description="text itme to be put in")
):  
  await interaction.response.defer()

  try:
    print(db[key])
    await interaction.followup.send(f"\"{key}\" aready exist in the database please use different key")
    return
  except:
    pass
                
  db[key] = text
  
  await interaction.followup.send(f"successfully put \"{key}\" into the database")



@bot.slash_command(
  name="get",
  description="get item from the database".strip(),
)
async def get(interaction: nextcord.Interaction,
              key : str = nextcord.SlashOption(required=True,
                                               description="text to get the item")) -> None:
  
  await interaction.response.defer()

  try:
    print(db[key])
  except:
    await interaction.followup.send(f"database doesn't contain item with a key \"{key}\"")
    return
  
  item = db[key]
              
  embed = nextcord.Embed()
  if "https://" in item or "http://" in item:
    embed.set_image(item)
  else:
    embed.set_footer(text=item)
  
  await interaction.followup.send(embed=embed)