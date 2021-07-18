import random

from discord.ext import commands
import discord

import file_utils
from logger import log
from config_reader import config
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-t", "--test", action="store_true", help="post to discord test server")

args = parser.parse_args()

bot = commands.Bot(command_prefix='!')

trees = file_utils.read_csv(config['trees_path'])

print('trees:', trees)
print('trees: len', len(trees))


@bot.event
async def on_ready():
    # await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=""))
    log('we have logged in as {0.user}'.format(bot))


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if '!treeteller' in message.content.lower():
        tree = trees[random.randint(0, len(trees))]

        name = tree[1] if tree[1] != '' and tree[1] != '-' else "Unknown"
        species = tree[2] if tree[2] != '' and tree[2] != '-' else "Unknown"
        age = tree[3] if tree[3] != '' and tree[3] != '-' else "Unknown"
        location = tree[4] if tree[4] != '' and tree[4] != '-' else "Unknown"
        description = tree[6] if tree[6] != '' and tree[6] != '-' else "Unknown"

        embed = discord.Embed(title=name, colour=discord.Colour.random())
        embed.add_field(name="Species", value=species, inline=False)
        embed.add_field(name="Age", value=age, inline=False)
        embed.add_field(name="Location", value=location, inline=False)
        embed.add_field(name="Description", value=description, inline=False)
        await message.channel.send(embed=embed)

if args.test:
    credential_key = 'test-server'
else:
    credential_key = 'abs-arb'

bot.run(config['credentials'][credential_key]['discord_token'])
