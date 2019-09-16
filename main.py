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
    if message.content.startswith("%addmeme"):
        await message.channel.send("DM micahlt#4835 for your memes to be added to the bot.")
    if message.content.startswith("%help"):
        await message.channel.send("All commands start with a percent sign.")
        await message.channel.send("Commands: meme, help, ver, hello, addmeme, and more soon!")
        await message.channel.send("Developed by Micah Lindley")
    if message.content.startswith("%meme"): 
        memeNumber = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
        meme = random.choice(memeNumber)
        await message.channel.send(file=discord.File('memes/' + meme + '.jpg'))
        await message.channel.send(file=discord.File('memes/' + meme + '.png'))

client.run(os.environ['TOKEN'])
