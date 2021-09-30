import discord
from discord.ext import commands
import config
import os

client = commands.Bot( command_prefix = '.' )
client.remove_command("help")

@client.event 

async def on_ready():
    print( 'BOT connected' )


@client.command()
async def load(ctx, extension):
    if ctx.author.id == 379642060661063689:
        client.load_extension(f"cogs.{extension}")
        await ctx.send("Cogs is loaded...")
    else:
        await ctx.send("Ты че еблан?")

@client.command()
async def unload(ctx, extension):
    if ctx.author.id == 379642060661063689:
        client.unload_extension(f"cogs.{extension}")
        await ctx.send("Cogs is unloaded...")
    else:
        await ctx.send("Ты че еблаsн?")


@client.command()
async def reload(ctx, extension):
    if ctx.author.id == 379642060661063689:
        client.unload_extension(f"cogs.{extension}")
        client.load_extension(f"cogs.{extension}")
        await ctx.send("Cogs is loaded...")
    else:
        await ctx.send("Ты че еблан?")

for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        client.load_extension(f"cogs.{filename[:-3]}")



client.run(config.TOKEN)