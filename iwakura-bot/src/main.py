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
from discord import user
import requests

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


## Seems that bot cant message users with no relashionship to them.
## So if the user is kicked of banned from the channel, this bound is unamade,
## and discord API returns a 403 error.

#@client_discord.event
#async def on_member_remove(user):
#    channel = None
#    await iwakura.trigger_achievement(user.id, Heresy)

    #for chn in user.guild.channels:
    #    if (chn.position == 0 or chn.name == 'geral') and chn.type.name == 'text':
    #        channel = chn
    #        break
    #
    #await channel.send('https://media.discordapp.net/attachments/372809185483685899/857738774054174760/klipartz.com_2.png?width=300&height=670')
    #await channel.send(f'{user.display_name} HAS BEEN **EXECUTED**,\nMay god have mercy of this soul.')
    #time.sleep(8)
    #await channel.send('PARTY TIME!!! https://www.youtube.com/watch?v=TDyG4YNUXcI')


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
async def on_voice_state_update(member, before, after):
    """
    Triggered when a user joins at a voice channel
    """

    users_before = []
    users_after = []
    if before.channel is not None and before.channel.members is not None:
        users_before = [buser.id for buser in before.channel.members]
        
    if after.channel is not None and after.channel.members is not None:
        users_after = [auser.id for auser in after.channel.members]
        
    joined = list(set(users_after) - set(users_before))
    for user_id in joined:
        await iwakura.trigger_achievement(user_id, HappyHour)


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
    
    ## For some reason, discord does not provide the old version of user avatar.
    ## So, as far as i know, there is no way to detect the event of avatar change,
    ## since mutiple actions are bound to this API call.
    #
    # Triggering achievements based on avatar
    #
    # I have to compare them based on bytes,
    # because discord uses the same url for all user profile pictures
    # bimage = requests.get('https://cdn.discordapp.com' + before.avatar_url._url, stream=True).content
    # aimage = requests.get('https://cdn.discordapp.com' + after.avatar_url._url, stream=True).content

    # if bimage != aimage:
    #    await iwakura.trigger_achievement(after.id, Doppleganger)

    # Triggering achievements based on roles
    if not after.bot:
        await iwakura.trigger_achievement(after.id, BurnTheImpostor, args=[after.display_name])
        await iwakura.trigger_achievement(after.id, LeaveTheDoorOpen, args=[config, roles_gained])
        await iwakura.trigger_achievement(after.id, MyHouseMyLife, [config, roles_gained])
        await iwakura.trigger_achievement(after.id, SOFAMOUS, [config, roles_gained])
        await iwakura.trigger_achievement(after.id, BloodStained, [config, roles_gained])
        await iwakura.trigger_achievement(after.id, Blessed, [config, roles_gained])
        await iwakura.trigger_achievement(after.id, Congratulations, [config, roles_gained])
        await iwakura.trigger_achievement(after.id, BrainWashed, [config, roles_gained])
        await iwakura.trigger_achievement(after.id, UnForastero, [config, roles_gained])
        await iwakura.trigger_achievement(after.id, Ni, [config, roles_gained])


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
        await iwakura.trigger_achievement(message.author.id, JoinTheBowdyHouse, args=[config, message])

        # Based on message content
        await iwakura.trigger_achievement(message.author.id, HeraldIntern, args=[message.content])
        await iwakura.trigger_achievement(message.author.id, AncientKnowledge, args=[message.content])
        await iwakura.trigger_achievement(message.author.id, TheJester, args=message)
        await iwakura.trigger_achievement(message.author.id, Lvl20Bard, args=message)
        await iwakura.trigger_achievement(message.author.id, Charge, args=message)

        # Based on channel
        await iwakura.trigger_achievement(message.author.id, BeastMaster, args=[config, message])
        
        # No requirement
        await iwakura.trigger_achievement(message.author.id, PigeonIntern)
        await iwakura.trigger_achievement(message.author.id, PigeonMaster)
        await iwakura.trigger_achievement(message.author.id, PigeonCelebrity)
        await iwakura.trigger_achievement(message.author.id, PigeonNoble)
        await iwakura.trigger_achievement(message.author.id, PigeonDeity)
        await iwakura.trigger_achievement(message.author.id, WheelOfFortune, args=[message.content])

        # Sending links
        await iwakura.trigger_achievement(message.author.id, CanineHero, args=[message.content])
        
        
client_discord.run(config.get_attr('api', 'discord_token'))