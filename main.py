import discord
from discord.ext import commands

bot = commands.Bot(command_prefix="!!", intents=discord.Intents.all())


@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')


@bot.command()
async def tempalato(ctx):
    ...


bot.run("MTA5NzE5OTc2NDIyMDY3NDA2OQ.GKJ8_1.ouDHjBXyzpVdVJwE9NiMR3hRHG_38uy43y6Nzk")  # TODO: get gud kid
sdfgsdfsdfsdf