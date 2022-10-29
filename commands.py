from setup import *
from utils import uri_validator, construct_embed


@bot.slash_command(
  name="put",
  description="put item into the database",
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
    embed = construct_embed(text=f"\"{key}\" already exist in the database please use different key")
    await interaction.followup.send(embed=embed)
    return
  except:
    pass
  
  db[key] = attachment.url
  
  embed = construct_embed(text=f"successfully put \"{key}\" into the database")
  await interaction.followup.send(embed=embed)



@bot.slash_command(
  name="put_text",
  description="put text item into the database",
)
async def put_text(interaction: nextcord.Interaction,
              key : str = nextcord.SlashOption(required=True,
                                               description="text that will be used to get the item"),
              text : str = nextcord.SlashOption(required=True,
                                                description="text item to be put in")
):  
  await interaction.response.defer()

  try:
    print(db[key])
    embed = construct_embed(text=f"\"{key}\" already exist in the database please use different key")
    await interaction.followup.send(embed=embed)
    return
  except:
    pass
                
  db[key] = text

  embed = construct_embed(text=f"successfully put \"{key}\" into the database")
  await interaction.followup.send(embed=embed)



@bot.slash_command(
  name="get",
  description="get item from the database",
)
async def get(interaction: nextcord.Interaction,
              key : str = nextcord.SlashOption(required=True,
                                               description="text to get the item")
):  
  await interaction.response.defer()

  try:
    print(db[key])
  except:
    embed = construct_embed(text=f"database doesn't have item with a key \"{key}\"")
    await interaction.followup.send(embed=embed)
    return
  
  item = db[key]
                                                 
  if uri_validator(item):
    embed = construct_embed(image_url=item)
  else:
    embed = construct_embed(text=item)
    embed.set_footer(text=item)
  
  await interaction.followup.send(embed=embed)