import discord
from discord.ext import commands

bot = commands.Bot("")

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

@bot.command()
async def stop(ctx):
    ...


bot.run("")  # TODO: add token
