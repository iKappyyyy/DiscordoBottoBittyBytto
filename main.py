import discord
from discord.ext import commands
from os import environ

bot = commands.Bot(command_prefix="!!", intents=discord.Intents.all())
TOKEN = environ.get('discordo_token')

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')


@bot.command(name="tempalato")
async def tempalato(ctx):
    ...


bot.run(TOKEN)
