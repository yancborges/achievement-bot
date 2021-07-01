"""
Iwakura bot source code.
This sript runs discord bot instance. You need to have an .env file
with your bot tokens when running this scripts
Running it allows bot to connect to discord automatically.
"""

import os
import discord
import re
import time

from discord.ext.commands import Bot
from discord.ext import commands

from models.Bot import Bot
from models.BehaviorAchievements import *
from models.Commands import *
from models.InternalConfigs import InternalConfigs


# Discord configuration
intents = discord.Intents.default()
intents.members = True

# Instancing objects
config = InternalConfigs()
client_discord = commands.Bot(command_prefix=config.get_attr('api', 'discord_token'), intents=intents)
iwakura = Bot(client_discord, config.get_attr('global', 'environment'), config)
cmd = IwakuraCommands(client_discord, iwakura)
PREFIX = config.get_attr('discord', 'cmd_prefix')


@client_discord.event
async def on_member_remove(user):
    channel = None
    for chn in user.guild.channels:
        if (chn.position == 0 or chn.name == 'geral') and chn.type.name == 'text':
            channel = chn
            break

    await channel.send('https://media.discordapp.net/attachments/372809185483685899/857738774054174760/klipartz.com_2.png?width=300&height=670')
    await channel.send(f'{user.display_name} HAS BEEN **EXECUTED**,\nMay god have mercy of this soul.')
    time.sleep(8)
    await channel.send('PARTY TIME!!! https://www.youtube.com/watch?v=TDyG4YNUXcI')


@client_discord.event
async def on_ready():
    """
    Triggered when bot successfully connects to discord api
    """

    print(f'{client_discord.user} has connected to Discord!')


@client_discord.event
async def on_member_join(member):
    """
    Triggered when a member joins the server
    """

    await iwakura.trigger_achievement(member.id, YouAreFinallyAwake)


@client_discord.event
async def on_raw_reaction_add(payload):
    """
    Triggered when a emoji/reaction is added to a message
    """

    if not payload.member.bot:
        await iwakura.trigger_achievement(payload.member.id, Mimic)


@client_discord.event
async def on_message_edit(before, after):
    """
    Triggered whenever a message is edited
    """

    # Ignoring interactions with other bots
    if not after.author.bot:
        await iwakura.trigger_achievement(after.author.id, TimeTraveler)


@client_discord.event
async def on_message_delete(message):
    """
    Triggered whenever a message is deleted
    """

    # Ignoring interactions with other bots
    if not message.author.bot:
        await iwakura.trigger_achievement(message.author.id, LibraryOfAlexandria)
        await iwakura.trigger_achievement(message.author.id, MisleadLatter)


@client_discord.event
async def on_member_update(before, after):
    """
    Event triggered when user changes:
    - status
    - nick
    - profile avatar
    - roles

    Parameters
    ----------

    before : User
        User instance before event triggers
    after : User
        User instance after event triggers
    """
    
    # Getting changed roles
    role_changed = None
    roles_before = [brole.id for brole in before.roles]
    roles_after = [arole.id for arole in after.roles]

    roles_gained = [r for r in roles_after if r not in roles_before]
    roles_lost = [r for r in roles_before if r not in roles_after]
    
    # Triggering achievements based on roles
    if config.get_attr('custom', 'bunda_mole') in roles_gained:
        # TODO: use class here
        pass

@client_discord.event
async def on_message(message):    
    """
    Triggered when a message is sent
    on any channel where bot has access to read from
    """
    
    if message.author.bot:
        # Ignoring interactions with other bots
        return
    if message.content.startswith(PREFIX):
        await cmd.manage(message)
    else:
        
        # Based on category
        if hasattr(message.channel, 'category') and message.channel.category.id == config.get_attr('custom', 'lewd_category'):
            for att in message.attachments:
                if re.findall(r'(\.((png)|(jpeg)|(jpg)|(gif)))$', att.url):
                    await iwakura.trigger_achievement(message.author.id, JoinTheBowdyHouse)

        # Based on message content
        if re.findall(r'<@!\d+>', message.content):
            await iwakura.trigger_achievement(message.author.id, HeraldIntern)

        if '!kdgauga' in message.content or '!diegao' in message.content:
            await iwakura.trigger_achievement(message.author.id, AncientKnowledge)

        if 'k' in message.content:
            await iwakura.trigger_achievement(message.author.id, TheJester, args=message)

        # Based on channel
        if message.channel.id == config.get_attr('custom', 'pokemon_channel'):
            await iwakura.trigger_achievement(message.author.id, BeastMaster)
        
        # No requirement
        await iwakura.trigger_achievement(message.author.id, PigeonIntern)
        await iwakura.trigger_achievement(message.author.id, PigeonMaster)
        await iwakura.trigger_achievement(message.author.id, PigeonCelebrity)
        await iwakura.trigger_achievement(message.author.id, PigeonNoble)
        await iwakura.trigger_achievement(message.author.id, PigeonDeity)
        await iwakura.trigger_achievement(message.author.id, WheelOfFortune, args=[message.content])
        
        
client_discord.run(config.get_attr('api', 'discord_token'))