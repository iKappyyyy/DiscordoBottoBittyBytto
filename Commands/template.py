from discord.ext import commands

@commands.command(name="template")
async def where(ctx, message):
    ...

async def setup(bot):
    bot.add_command(where)
