import discord
import filereader
import rankrequirement
from sayings import SCOUTOATH, SCOUTLAW, OUTDOORCODE, PLEDGE
#from localsayings import *

f = open('token.cfg')
token = f.readline()
f.close()

client = discord.Client()
PREFIX = '!'

RANKFILESDIR = 'rankfiles'

FILESTOREAD = ['scout.txt', 'tenderfoot.txt', \
               'secondclass.txt', 'firstclass.txt', \
               'star.txt', 'life.txt', 'eagle.txt']

FILESTOREAD = list(map(lambda file: RANKFILESDIR + "/" + file, FILESTOREAD))

rankData = filereader.readRankData(FILESTOREAD)


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print('------')

@client.event
async def on_message(message):
    if message.author.bot:
        pass
    else:
        if message.content.startswith(PREFIX + 'help'):
            await message.channel.send(\
                    'Available commands: pledge rank scoutoath scoutlaw outdoorcode')
        elif message.content.startswith(PREFIX + 'rank'):
            await message.channel.send(rankrequirement.rankRequirement(message.content, rankData))
        elif message.content.startswith(PREFIX + 'scoutoath'):
            await message.channel.send(SCOUTOATH)
        elif message.content.startswith(PREFIX + 'scoutlaw'):
            await message.channel.send(SCOUTLAW)
        elif message.content.startswith(PREFIX + 'outdoorcode'):
            await message.channel.send(OUTDOORCODE)
        elif message.content.startswith(PREFIX + 'pledge'):
            await message.channel.send(PLEDGE)
        elif message.content.startswith(PREFIX):
            await message.channel.send("Usage: !command (!help for available commands)")

client.run(token)
