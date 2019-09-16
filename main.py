import os
import discord
import random

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('%hello'):
        await message.channel.send('Hello!  SqueakyMeme is up and running!')
    if message.content.startswith('%ver'):
        await message.channel.send('0.1.1') 
    if message.content.startswith("%rec"):
        await message.channel.send("DM micahlt#4835 for your memes to be added to the bot.")
    if message.content.startswith("%info"):
        await message.channel.send("All commands start with a dollar sign.")
        await message.channel.send("Commands: info, ver, hello, rec, and more soon!")
        await message.channel.send("Developed by Micah Lindley")
    if message.content.startswith("%meme"): 
        memeNumber = ['0', '1', '2', '3', '4', '5']
        meme = '0'
        await message.channel.send(file=discord.File('https://raw.githubusercontent.com/micahlt/sm-bot/master/memes/' + meme + '.jpg'))
        print('https://raw.githubusercontent.com/micahlt/sm-bot/master/memes/' + meme + '.jpg')

client.run(os.environ['TOKEN'])
