import discord
from discord.ext import commands
from os import environ

bot = commands.Bot(command_prefix="!!", intents=discord.Intents.all(), activity=discord.Game("In The Hunger Games"))
TOKEN = environ.get("DISCORDO_BOTTO_TOKEN")

BOT_ID = 1097199764220674069


@bot.event
async def on_ready():
    print(f"{bot.user} has connected to Discord!")
    bot.load_extension('Commands.where')


@bot.command(name="tempalato")
async def tempalato(ctx):
    ...


@bot.command(name="default")
async def default_traits(ctx):
    """
    Sets bot's traits back to original pfp and name.
    """

    with open("./Default_Traits/Default_PFP.png", "rb") as image:
        await bot.user.edit(avatar=image.read())

    with open("./Default_Traits/Default_Name.txt", "r") as name:
        bot_member = ctx.guild.get_member(BOT_ID)
        await bot_member.edit(nick=name.read())


@bot.command(aliases=["BeMe!!", "beme!!", "bm", "bm!!", "BEME!!"])
async def change_traits_to_user(ctx):
    """
    Sets bot's traits to the user that used the command.
    """

    # change pfp
    await ctx.author.avatar.save("User_PFP.png")
    with open("./User_PFP.png", "rb") as image:
        await bot.user.edit(avatar=image.read())

    # change name
    bot_member = ctx.guild.get_member(BOT_ID)
    await bot_member.edit(nick=ctx.author.name)

    await ctx.send("I\'m you now! great...")


bot.run(TOKEN)
