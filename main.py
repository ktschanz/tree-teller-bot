import random

from discord.ext import commands
import discord
import traceback

import file_utils
from logger import log
from config_reader import config
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-t", "--test", action="store_true", help="post to discord test server")

args = parser.parse_args()

bot = commands.Bot(command_prefix='!')

trees = file_utils.read_csv(config['trees_path'])
speciess = file_utils.read_csv(config['species_path'])

log('trees:', trees)
log('trees: len', len(trees))
log('species:', speciess)
log('species: len', len(speciess))


@bot.event
async def on_ready():
    # await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=""))
    log('we have logged in as {0.user}'.format(bot))


@bot.event
async def on_message(message):
    try:
        if message.author == bot.user:
            return
        if '!treeteller' in message.content.lower():
            log(f'received !species request from {message.author}')
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
        if '!species' in message.content.lower():
            log(f'received !species request from {message.author}')
            species = speciess[random.randint(0, len(speciess))]

            name = species[0] if species[0] != '' and species[0] != '-' else "Unknown"
            status = species[1] if species[1] != '' and species[1] != '-' else "Unknown"
            sci_name = species[2] if species[2] != '' and species[2] != '-' else "Unknown"
            size = species[3] if species[3] != '' and species[3] != '-' else "Unknown"
            habitat = species[4] if species[4] != '' and species[4] != '-' else "Unknown"
            image = species[5] if species[5] != '' and species[5] != '-' else "Unknown"

            embed = discord.Embed(title=name, colour=discord.Colour.random())
            embed.set_image(url=image)
            embed.add_field(name="Status", value=status, inline=False)
            embed.add_field(name="Latin Name", value=sci_name, inline=False)
            embed.add_field(name="Size", value=size, inline=False)
            embed.add_field(name="Habitat", value=habitat, inline=False)
            await message.channel.send(embed=embed)
    except:
        log(traceback.format_exc())

if args.test:
    credential_key = 'test-server'
else:
    credential_key = 'abs-arb'

bot.run(config['credentials'][credential_key]['discord_token'])
