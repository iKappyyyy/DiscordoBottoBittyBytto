import discord
from discord.ext import commands
from os import environ

bot = commands.Bot(command_prefix="!!", intents=discord.Intents.all(), activity=discord.Game("In The Hunger Games"))
TOKEN = environ.get('DISCORDO_BOTTO_TOKEN')


@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')


@bot.command(name="tempalato")
async def tempalato(ctx):
    ...


bot.run(TOKEN)  # TODO: get gud kid
