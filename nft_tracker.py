import discord
import os
import requests
import time
import asyncio
from dotenv import load_dotenv

opensea_url = "https://api.opensea.io/api/v1/asset/"
demonz_address = "0xae16529ed90fafc927d774ea7be1b95d826664e3"
goons_address = "0x8442dd3e5529063b43c69212d64d5ad67b726ea6"
kongs_address = "0xEf0182dc0574cd5874494a120750FD222FdB909a"
martians_address = "0x4961db588dd962abb20927aa38fa33e5225b3be2"
skulls_address = "0xb28a4fde7b6c3eb0c914d7b4d3ddb4544c3bcbd6"
warriors_address = "0xef9c21e3ba31a74910fc7e7cb3fc814ad842ad6e"
default_token = "1"

demonnz_floor = 0
goons_floor = 0
kongs_floor = 0
martians_floor = 0
skulls_floor = 0
warriors_floor = 0

def getFloor(address):
    response = requests.get(opensea_url + address + "/" + default_token)
    js = response.json()
    fp = js["collection"]["stats"]["floor_price"]
    return fp

def getStatus():
    kongs_floor = getFloor(kongs_address)
    martians_floor = getFloor(martians_address)
    warriors_floor = getFloor(warriors_address)
    value = "\U0001F412" + str(kongs_floor) + "|" + "\U0001F47D" + str(martians_floor) + "|" + "\U0001F9D9" + str(warriors_floor)
    return value

client = discord.Client()

async def status_task():
    while True:
        await client.change_presence(activity=discord.Game(name=getStatus()))
        await asyncio.sleep(300)

@client.event
async def on_ready():
    print('Logged on as {0.user}'.format(client))
##    await client.change_presence(activity=discord.Game(name=getStatus()))
    client.loop.create_task(status_task())

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$d'):
        demonz_floor = getFloor(demonz_address)
        await message.channel.send("Demonz Floor Is: " + str(demonz_floor))
        
    if message.content.startswith('$g'):
        goons_floor = getFloor(goons_address)
        await message.channel.send("Goons Floor Is: " + str(goons_floor))
        
    if message.content.startswith('$k'):
        kongs_floor = getFloor(kongs_address)
        await message.channel.send("Kongs Floor Is: " + str(kongs_floor))

    if message.content.startswith('$m'):
        martians_floor = getFloor(martians_address)
        await message.channel.send("Martians Floor Is: " + str(martians_floor))
       
    if message.content.startswith('$s'):
        skulls_floor = getFloor(skulls_address)
        await message.channel.send("Skvllpvnk Floor Is: " + str(skulls_floor))
 
    if message.content.startswith('$w'):
        warriors_floor = getFloor(warriors_address)
        await message.channel.send("Warriors Floor Is: " + str(warriors_floor))

if __name__ == "__main__":
    load_dotenv()
    client.run(os.getenv('TOKEN'))


