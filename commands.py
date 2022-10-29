from setup import *
from utils import uri_validator, construct_embed, get_raw_key


@bot.slash_command(
  name="put",
  description="put item into your database",
)
async def put(interaction: nextcord.Interaction,
              key : str = nextcord.SlashOption(required=True,
                                               description="text that will be used to get the item"),
              attachment: nextcord.Attachment = nextcord.SlashOption(required=True,
                                                                     description="item to be put in")
):  
  await interaction.response.defer()
  key = key.strip().lower()

  user_key = f"{key}.{str(interaction.user.id)}"
  
  try:
    print(db[user_key])
    embed = construct_embed(text=f"\"{key}\" already exist in your database please use different key or delete the item")
    await interaction.followup.send(embed=embed)
    return
  except:
    pass
  
  db[user_key] = attachment.url
  
  embed = construct_embed(text=f"successfully put \"{key}\" into your database")
  await interaction.followup.send(embed=embed)



@bot.slash_command(
  name="put_text",
  description="put text item into your database",
)
async def put_text(interaction: nextcord.Interaction,
              key : str = nextcord.SlashOption(required=True,
                                               description="text that will be used to get the item"),
              text : str = nextcord.SlashOption(required=True,
                                                description="text item to be put in")
):  
  await interaction.response.defer()
  key = key.strip().lower()

  user_key = f"{key}.{str(interaction.user.id)}"

  try:
    print(db[user_key])
    embed = construct_embed(text=f"\"{key}\" already exist in your database please use different key or delete the item")
    await interaction.followup.send(embed=embed)
    return
  except:
    pass
                
  db[user_key] = text

  embed = construct_embed(text=f"successfully put \"{key}\" into your database")
  await interaction.followup.send(embed=embed)



@bot.slash_command(
  name="get",
  description="get item from global database",
)
async def get(interaction: nextcord.Interaction,
              key : str = nextcord.SlashOption(required=True,
                                               description="item key, item with the same key will be choosen randomly")
):  
  await interaction.response.defer()
  key = key.strip().lower()
  
  items = db.prefix(key)
  
  if len(items) == 0:
    embed = construct_embed(text=f"the database doesn't have item with a key \"{key}\"")
    await interaction.followup.send(embed=embed)
    return
  
  item = db[random.choice(items)]
                                                 
  if uri_validator(item):
    embed = construct_embed(image_url=item)
  else:
    embed = construct_embed(text=item)
    embed.set_footer(text=item)
  
  await interaction.followup.send(embed=embed)



@bot.slash_command(
  name="delete",
  description="delete item from your database",
)
async def get(interaction: nextcord.Interaction,
              key : str = nextcord.SlashOption(required=True,
                                               description="item key for deletion")
):  
  await interaction.response.defer()
  key = key.strip().lower()

  user_key = f"{key}.{str(interaction.user.id)}"
  
  try:
    print(db[user_key])
  except:
    embed = construct_embed(text=f"your database doesn't have item with a key \"{key}\"")
    await interaction.followup.send(embed=embed)
    return
  
  del db[user_key]

  embed = construct_embed(text=f"successfully delete \"{key}\" from your database")
  await interaction.followup.send(embed=embed)