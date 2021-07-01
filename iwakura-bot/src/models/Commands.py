"""
Command class. Its goal it's to handle generically
all message commands currently and futurely added. Command class
uses a Bot class instance and discord client object.
Calling its command manage passing message event as argument
will self handle which command should be called.
"""

import re
import inspect
import random
from datetime import datetime

from .BehaviorAchievements import *
from .GivenAchievement import *
from .Quote import Quote
from .Exceptions import *
from .CustomCommand import CustomCommand

class IwakuraCommands:
    """
    Command class. Its goal its to handle commands based
    on text generically. instead of adding a logical operator for each
    new command.

    Parameters
    ----------

    discord_client : discord
        Discord client object

    iwakura_client : Bot
        Bot class instance
    """

    help_messages = {
        'showachievements': '**showachievements command.** It shows all achievements from a given user.\n\
**syntax:** >showachievement __@user__\'If user is none, shows your own achievements',
        'help': 'Seriously?',
        'gimme': '||It gives you an achievement||'
    }
    
    def __init__(self, discord_client, iwakura_client):
        self.discord_client = discord_client
        self.iwakura_client = iwakura_client
        self._cls_prefix = '_IwakuraCommands__cmd_'

    async def manage(self, message):
        """
        Manages the message to execute the correct
        commando function based on given text

        Parameters
        ----------

        message : discord.message
            message that triggered on_message event
        """
        context = message 
        text = message.content[1:]
        cmd = text.split(' ')[0]
        if not cmd:
            await context.channel.send(
                'Error. No command given. Use >help to see all commands'
            )
        args = re.findall(r'<[,\w\d!@\. \'\"\/:\-=\?]+>', text.split(cmd)[1])
        args = [a.replace('<','').replace('>','') for a in args]
        if ' ' in args:
            await context.channel.send(
                'Error. Argument is empty'
        )
        wrong_args = text.split(' ')
        if not args and len(wrong_args) > 1:
            await context.channel.send(
                'Error. command arguments must be used between < >. i.e: >showachievements <help>'
            )
            return

        self_members = inspect.getmembers(self)
        if args and args[0] == 'help':
            try:
                await context.channel.send(
                    self.help_messages[cmd]
                )
            except KeyError:
                await context.channel.send('This command is invalid or does not have any help doc')
            finally:
                return

        for _method in self_members:
            _method_path = _method[0]
            _method_name = _method_path.replace(self._cls_prefix, '')
            _method_function = _method[1]
            if _method_path.startswith(self._cls_prefix):
                if _method_name == cmd:
                    await _method_function(context, text, args)
                    return
        
        custom_cmd = self.iwakura_client.db_client.get(CustomCommand.TABLE_NAME, {'name': cmd})
        if custom_cmd:
            await context.channel.send(custom_cmd[0]["text"])
            return

        await context.channel.send('Error, unknown command. use >help for see all commands')

    def __allow_admin(func):          
        """
        Admin wraper. Blocks functions from being executed
        based on user roles.
        """
        async def inner(self, context, text, args):
            if context.author.id == self.iwakura_client.config.get_attr('custom', 'admin_id'):
                await func(self, context, text, args)
            else:
                await context.channel.send('This command is admin only, sorry :(')    
        return inner

    def __usr_as_argument(func):
        """
        User wraper. Validates if first argument is a  valid user mention
        """
        async def inner(self, context, text, args):
            if args:
                if not args[0].startswith('@!'):
                    await context.channel.send('Error. User must be a mention. Use @<user_name>')
                    return
                if isinstance(args[0], str):
                    args[0] = int(args[0][2:])
                # TODO: Try to fetch user here
            await func(self, context, text, args)
        return inner
            
    async def __cmd_help(self, context, text, args):
        """
        Help command. It shows all other commands
        iwakura has.
        """
        self_members = inspect.getmembers(self)
        cmds = [
            _m[0].replace(self._cls_prefix, '') for _m in self_members if _m[0].startswith(self._cls_prefix)
        ]
        cmds_str = ', '.join(cmds)
        msg = f'Commands: {cmds_str}.\nPrefix for all is \'>\'\nUse >__command__ <help> for command instructions'
        await context.channel.send(msg)
        
    async def __cmd_gimme(self, context, text, args):
        """
        Gives an achievement to the user
        """
        await self.iwakura_client.trigger_achievement(context.author.id, YouTried)

    async def __cmd_showachievements(self, context, text, args):
        """
        Shows to the user all achievements from the given user.
        syntax: >showachievements @user (optional)
        """
        target = None
        if args:
            target = int(args[0][2:])
        else:
            target = context.author.id
        await self.iwakura_client.show_achievements(context, target)
        await context.channel.send('Sent unlocked achievements via PM')

    async def __cmd_play(self, context, text, args):
        """
        Triggers Im a Rouge achievement and makes the bot
        join voice chat if user is connected. Otherwise
        the achievement is not triggered
        """

        # TODO: Join voice channel here, then leave sending a message
        await self.iwakura_client.trigger_achievement(context.author.id, ImARogue)

    @__allow_admin
    async def __cmd_health(self, context, text, args):
       """
       Says if she is ok
       """
       await context.channel.send('*Lain handshakes*')        

    async def __cmd_quit(self, context, text, args):
        """
        Closes client connection
        """
        await context.channel.send('*Lain gonna sleep, good night*')
        await self.discord_client.close()

    async def __cmd_disconnect(self, context, text, args):
        """
        Disconnect from all voice channels
        """
        for x in self.discord_client.voice_clients:
            if(x.server_id == context.channel.guild.id):
                await x.disconnect()

    @__usr_as_argument
    async def __cmd_award(self, context, text, args):
        """
        Triggers a GivenAchievement to the user passed as argument
        syntax: >award @user <achievement name> <achievement description>
        """
        # TODO: Make user argument multiple
        if len(args) < 3:
            await context.channel.send(
                'Invalid syntax, use: >award user_mention <achievement_name> <achievement_description>'
            )
            return
        
        await self.iwakura_client.trigger_achievement(context.author.id, GivenAchievement, args)
        await context.channel.send('Achievement has been given to the user. Congratz!')

    async def __cmd_kdgauga(self, context, text, args):
        """
        Send a message from Ariel
        """
        #layout = random.randint(1, 10)
        farm_a = random.randint(0,300)
        farm_b = random.randint(0,300)

        msg = f'{farm_a} a {farm_b}. to com o dobro de farm dela já'
        if farm_a / 2 == farm_b:
            await self.iwakura_client.trigger_achievement(context.author.id, MakeItDouble)
        await context.channel.send(msg)

    @__usr_as_argument
    async def __cmd_addquote(self, context, text, args):
        """
        Adds a quote to database
        syntax: >addquote @author <quote> <quote date [optional]>
        """
        if not args or len(args) > 2:
            await context.channel.send(
                'Error, wrong syntax. use >addquote @<user mention> <quote text> <quote date [optional]>'
            )
        author = args[0]
        quote = args[1]
        creation = args[2] if len(args) >= 3 else None
        creator = context.author.id
        if not creation:
            creation = datetime.today().utcnow().strftime('%Y-%m-%dT%H:%M:%S.%fZ')

        q = Quote(author, creator, quote, creation, self.iwakura_client.db_client)
        q.save()

        await context.channel.send('Quote saved')

    async def __cmd_quote(self, context, text, args):
        """
        Plays a random quote from the base
        """
        if not args:
            quotes = self.iwakura_client.db_client.get(Quote.TABLE_NAME, {})
            quotes = [q for q in quotes]
            _quote = random.choice(quotes)

            _creation = _quote["creation"]
            try:
                _creation = datetime.strptime(_creation, '%Y-%m-%dT%H:%M:%S.%fZ')
                _creation = _creation.strftime('%d/%m/%Y')
            except ValueError:
                pass
            _quote["author"] = await self.iwakura_client.discord_client.fetch_user(_quote["author_id"])
            _quote["creator"] = await self.iwakura_client.discord_client.fetch_user(_quote["creator_id"])
            msg = f'"_{_quote["quote"]}_"\n\t\t\t\t\t\t\t - **{_quote["author"].display_name}**, {_creation}'
        else:
            msg = 'Sorry, this part is not ready yet :('

        await context.channel.send(msg)

    async def __cmd_addcmd(self, context, text, args):
        """
        Adds a custom command to the base
        syntax: >addcmd <command name> <desired text>
        """
        if not args or len(args) < 2:
            await context.channel.send('Error, Wrong syntax. Use >addcmd <command name> <desired text>')
            return

        cmd_name = args[0]
        cmd_text = args[1]

        self_members = inspect.getmembers(self)
        for _method in self_members:
            _method_path = _method[0]
            _method_name = _method_path.replace(self._cls_prefix, '')
            _method_function = _method[1]
            if _method_path.startswith(self._cls_prefix):
                if _method_name == cmd_name:
                    await context.channel.send('Error, this command is already in use internally, you cannot use this one, sorry :(')
                    return

        ccmd = CustomCommand(cmd_name, cmd_text, context.author.id, self.iwakura_client.db_client)
        try:
            ccmd.save()
        except AlreadyInUse as ex:
            await context.channel.send(ex)
        else:
            await context.channel.send('Command saved successfully')

    async def __cmd_delcmd(self, context, text, args):
        """
        Deletes a command. User can only deletes removed created by theirself
        syntax: >delcmd <command name>
        """
        if not args:
            await context.channel.send('Error, Wrong syntax. Use >delcmd <command name>')
            return

        cmd_name = args[0]
        ccmd = CustomCommand(cmd_name, '', context.author.id, self.iwakura_client.db_client)
        try:
            ccmd.delete()
        except NotFoundCommand as ex:
            await context.channel.send(ex)
        else:
            await context.channel.send('Command removed successfully')
            
        