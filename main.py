import json
import requests
import discord
from discord import colour
from discord.ext import commands
from discord.flags import Intents
import config
import os

client = commands.Bot(command_prefix = '.', intents=discord.Intents.all())
client.remove_command("help")

# BOT Activity
@client.event 
async def on_ready():
    print( 'BOT connected' )
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="за игроками"))

# Auto role/Connect new player
@client.event
async def on_mebmer_join(member):
    channel = client.get_channel(687981936802922524)

    role = discord.utils.get(member.guild.roles, id = 687980847919398924)

    await member.add_roles( role )
    await channel.send( emb = discord.Embed( description = f"Пользователь { member.mention }, присоеденился к нам!", colour =  0x005fff) )

# Cogs load/unload/reload ######################################################################
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
####################################################################################################

# Send DM message 
@client.command()
async def ls(ctx, member:discord.Member,*, arg):
    await ctx.message.delete()
    emb = discord.Embed(description=arg, color= 0x005fff)
    emb.set_author(name=ctx.author.name, icon_url = ctx.author.avatar_url)

    await member.send(embed = emb)
    emb = discord.Embed(description='**Сообщение отправленно!**', color= 0x005fff)
    await ctx.send(embed = emb)

# GAME
@client.command()
async def game(ctx):
	data = {
		"max_age": 86400,
		"max_uses": 0,
		"target_application_id": 814288819477020702, # Fishington.io
		"target_type": 2,
		"temporary": False,
		"validate": None
	}
	headers = {
		"Authorization": "Bot NzM4MzE0NDEzMTA2Mzk3MTg0.XyKG4Q.eBGiu5YECqFUBaMvaifxcd9Qr8U",
		"Content-Type": "application/json"
	}

	if ctx.author.voice is not None:
		if ctx.author.voice.channel is not None:
			channel = ctx.author.voice.channel.id
		else:
			await ctx.send("Зайдите в канал")
	else:
		await ctx.send("Зайдите в канал")

	response = requests.post(f"https://discord.com/api/v8/channels/{channel}/invites", data=json.dumps(data), headers=headers)
	link = json.loads(response.content)

	await ctx.send(f"https://discord.com/invite/{link['code']}")

# BOT Run
client.run(config.TOKEN)