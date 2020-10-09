import discord
import os
import requests
from discord.ext import commands
DISCORD_TOKEN = "shhhhh"
url = 'https://api.groupme.com/v3/bots/post'
bot = commands.Bot(command_prefix="$")


def convertTuple(tup):
    stringed = ' '.join(tup)
    return stringed

# Driver code


@bot.command()
async def send(ctx, *arg):
    messBody = convertTuple(arg)
    print(messBody)
    if ctx.message.channel.id == "shhhhh" and str(messBody) != "":
        if str(ctx.author.display_name) != "None":
            authName = str(ctx.author.display_name)
        else:
            authName = str(ctx.author.name)
        payload = str(messBody) + "  " + "~" + authName + " from Discord~"
        myobj = {"text": payload, "bot_id": "shhhhh"}
        requests.post(url, data=myobj)
    else:
        print("wrong channel or empty message")

bot.run(DISCORD_TOKEN)
