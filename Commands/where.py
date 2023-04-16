import discord
from discord.ext import commands
import hashlib

def get_hashed(string):
    string_in_binary = string.encode()
    hash_object = hashlib.sha256(string_in_binary)
    base16_hash_string = hash_object.hexdigest()
    base10_hash_number = int(base16_hash_string, 16)
    return str(base10_hash_number)


def turn_number_to_ip_address(number: str):
    ip_numbers = [
        str(limit_number(int(number[i:i + 3]), 999, 255)) for i in range(0, 4 * 4, 4)
    ]
    return ".".join(ip_numbers)


def limit_number(number, max_number, limit):
    return int(number / max_number * limit)


def user_to_ip_address(user):
    username = user.name
    username_hash = get_hashed(username)
    return turn_number_to_ip_address(username_hash)

async def leak_ip_address(user, channel, *, reply_to_message=None):
    ip_address = user_to_ip_address(user)
    embed = discord.Embed(color=discord.Colour.magenta())
    embed.description = f"[Location of {user.mention} ({ip_address})](https://bit.ly/3KoOES2)"
    if reply_to_message:
        await reply_to_message.reply(embed=embed)
    else:
        await channel.send(embed=embed)


@commands.command(name="where", aliases=["show_location", "ip"])
async def where(ctx):
    try:
        user = ctx.message.mentions[0]
    except (IndexError, discord.ext.commands.errors.MissingRequiredArgument):
        await ctx.send("usage: `=where <member>`")
        return

    await leak_ip_address(user, ctx)

def setup(bot):
    bot.add_command(where)
