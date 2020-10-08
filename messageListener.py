import discord
import os
import requests
from discord.ext import commands
DISCORD_TOKEN = "shhhhhhh"
url = 'https://api.groupme.com/v3/bots/post'
bot = commands.Bot(command_prefix="$")
@bot.command()
async def send(ctx, arg):
  if ctx.message.channel.id == "shhhhhhh" and str(arg) != "":
    if str(ctx.author.display_name) != "None":
      authName = str(ctx.author.display_name)
    else:
      authName =str(ctx.author.name)
    payload = arg + "  "+ "~"+ authName + " from Discord~"
    myobj = {"text" : payload, "bot_id" : "shhhhhhh"}
    requests.post(url, data = myobj)
  else:
    print("wrong channel or empty message")

bot.run(DISCORD_TOKEN)
