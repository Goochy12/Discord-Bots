import discord
import os
import requests
import asyncio
from dotenv import load_dotenv

client = discord.Client()
channel = None
load_command = False

@client.event
async def on_ready():
    print('Logged on as {0.user}'.format(client))

## def 

def run_command():
    if load_command == True:
        channel.send(".play Before I Knew It Mason Ramsey")
        return

@client.event
async def on_voice_state_update(member, before, after):
    await member.guild.text_channels[0].send(str(member) + " joined the channel")

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$channel'):
        channel = message.channel
        await message.guild.text_channels[0].send(str(message.author) + " joined the channel")
        await message.guild.text_channels[0].send(";;play nickelback")
        ## await channel.send('Voice bot default message channel has been set to -> ' + str(channel))

if __name__ == "__main__":
    load_dotenv()
    client.run(os.getenv('VOICE_BOT_TOKEN'))
