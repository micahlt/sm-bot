from discord.ext import commands
import discord
import random, os

client = commands.Bot(command_prefix="$")

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'.lower()):
        await message.channel.send('Hello!  SqueakyMeme is up and running')
    if message.content.startswith('$ver'):
            await message.channel.send('0.1.1')
    if message.content.startswith("$add".lower()):
        await message.channel.send("Visit https://squeakymeme.ml/ to add your memes to the bot!")
    if message.content.startswith("$info".lower()):
        await message.channel.send("All commands start with a dollar sign.")
        await message.channel.send("Commands: info, ver, hello, rec, and more soon!")
        await message.channel.send("Developed by micahlt#4835 and smileycreations15#0215")
"""
client.remove_command("help")
@client.command(name="help")
async def help(ctx):
	ctx.channel.send("help")

@client.command(name="name")
async def command(ctx):
	pass
"""
client.run(os.environ['TOKEN'])
