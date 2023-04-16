from discord.ext import commands


@commands.command(name="template")
async def template(ctx, message):
    await ctx.send()


def setup(bot):
    bot.add_command(template)
