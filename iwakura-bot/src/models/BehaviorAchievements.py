"""
Class models for achievements unlocked by user actions.
All achievements inherits BaseModel.Achievement class.
"""

import random
import re

from discord import message
from .BaseModel import Achievement

class YouTried(Achievement):
    """
    You tried achievement. Given when user asks for it, using
    >gimme command.

    Parameters
    ----------

    discord_user_id : int
        Discord user id from user which triggered the achievement

    db_client : DbClient
        Instance of DbClient class

    args : list [Optional]
        List of additional args
    """
    
    score_total = 1
    achievement_name = 'You tried'
    achievement_description = 'Here\'s a consolation prize..'
    achievement_earning = 'Earned by asking for achievements to IwakuraBot'
    
    def __init__(self, discord_user_id, db_client, args=None):
        self.args = args
        super().__init__(discord_user_id, self.achievement_name, self.achievement_description,
             self.score_total, self._score, db_client
        )


    def _score(self):
        self.score_current += 1


class JoinTheBowdyHouse(Achievement):
    """
    Join the bowdy house achievement.
    Triggered when user uploads a picture to a specific
    text channel category.

    Parameters
    ----------

    discord_user_id : int
        Discord user id from user which triggered the achievement

    db_client : DbClient
        Instance of DbClient class

    args : list [Optional]
        List of additional args
    """

    score_total = 10
    achievement_name = 'Join the bowdy house'
    achievement_description = 'I know, you haven\'t been here'
    achievement_earning = 'Earned by sending 10 images at lewd channels'

    def __init__(self, discord_user_id, db_client, args=None):
        self.args = args
        super().__init__(discord_user_id, self.achievement_name, self.achievement_description,
             self.score_total, self._score, db_client
        )

    def verify(self):
        valid_images = 0
        config = self.args[0]
        message = self.args[1]
        if hasattr(message.channel, 'category') and message.channel.category.id == config.get_attr('custom', 'lewd_category'):
            for att in message.attachments:
                if re.findall(r'(\.((png)|(jpeg)|(jpg)|(gif)))$', att.url):
                    valid_images += 1
        return valid_images

    def _score(self):
        valids = self.verify()
        if valids:
            self.score_current += valids


class HeraldIntern(Achievement):
    """
    Heral intern achievement. Triggered each time
    a user mentions other user

    Parameters
    ----------

    discord_user_id : int
        Discord user id from user which triggered the achievement

    db_client : DbClient
        Instance of DbClient class

    args : list [Optional]
        List of additional args
    """

    score_total = 50
    achievement_name = 'Herald intern'
    achievement_description = 'By the order of Lord Farquaad, I am authorised to place you under arrest'
    achievement_earning = 'Earned by mentioning someone 50 times'
    
    def __init__(self, discord_user_id, db_client, args=None):
        self.args = args
        super().__init__(discord_user_id, self.achievement_name, self.achievement_description,
             self.score_total, self._score, db_client
        )

    def verify(self):
        if re.findall(r'<@!\d+>', self.args[0]):
            return True
        return False

    def _score(self):
        if self.verify():
            self.score_current += 1


class PigeonIntern(Achievement):
    """
    Pigeon intern achievement. Triggered each
    time a menssage is sent for a human user

    Parameters
    ----------

    discord_user_id : int
        Discord user id from user which triggered the achievement

    db_client : DbClient
        Instance of DbClient class

    args : list [Optional]
        List of additional args
    """

    score_total = 10
    achievement_name = 'Pigeon intern'
    achievement_description = 'Pru pru'
    achievement_earning = 'Earned by sending 10 messages'
    
    def __init__(self, discord_user_id, db_client, args=None):
        self.args = args
        super().__init__(discord_user_id, self.achievement_name, self.achievement_description,
             self.score_total, self._score, db_client
        )


    def _score(self):
        self.score_current += 1


class PigeonMaster(Achievement):
    """
    Pigeon master achievement. Triggered each
    time a menssage is sent for a human user

    Parameters
    ----------

    discord_user_id : int
        Discord user id from user which triggered the achievement

    db_client : DbClient
        Instance of DbClient class

    args : list [Optional]
        List of additional args
    """

    score_total = 100
    achievement_name = 'Pigeon master'
    achievement_description = 'I know things about pigeons, Lilly'
    achievement_earning = 'Earned by sending 100 messages'
    

    def __init__(self, discord_user_id, db_client, args=None):
        self.args = args
        super().__init__(discord_user_id, self.achievement_name, self.achievement_description,
             self.score_total, self._score, db_client
        )


    def _score(self):
        self.score_current += 1


class PigeonCelebrity(Achievement):
    """
    Pigeon celebrity achievement. Triggered each
    time a menssage is sent for a human user

    Parameters
    ----------

    discord_user_id : int
        Discord user id from user which triggered the achievement

    db_client : DbClient
        Instance of DbClient class

    args : list [Optional]
        List of additional args
    """

    score_total = 1000
    achievement_name = 'Pigeon celebrity'
    achievement_description = 'Pru pru'
    achievement_earning = 'Earned by sending 1000 messages'
    

    def __init__(self, discord_user_id, db_client, args=None):
        self.args = args
        super().__init__(discord_user_id, self.achievement_name, self.achievement_description,
             self.score_total, self._score, db_client
        )


    def _score(self):
        self.score_current += 1


class PigeonNoble(Achievement):
    """
    Pigeon noble achievement. Triggered each
    time a menssage is sent for a human user

    Parameters
    ----------

    discord_user_id : int
        Discord user id from user which triggered the achievement

    db_client : DbClient
        Instance of DbClient class

    args : list [Optional]
        List of additional args
    """

    score_total = 100000
    achievement_name = 'Pigeon noble'
    achievement_description = 'It\'s people i don\'t understand'
    achievement_earning = 'Earned by sending 100,000 messages'
    
    def __init__(self, discord_user_id, db_client, args=None):
        self.args = args
        super().__init__(discord_user_id, self.achievement_name, self.achievement_description,
             self.score_total, self._score, db_client
        )


    def _score(self):
        self.score_current += 1

    
class PigeonDeity(Achievement):
    """
    Pigeon deity achievement. Triggered each
    time a menssage is sent for a human user

    Parameters
    ----------

    discord_user_id : int
        Discord user id from user which triggered the achievement

    db_client : DbClient
        Instance of DbClient class

    args : list [Optional]
        List of additional args
    """

    score_total = 1000000
    achievement_name = 'Pigeon deity'
    achievement_description = 'Pru pru'
    achievement_earning = 'Earned by sending 1,000,000 messages'
    
    def __init__(self, discord_user_id, db_client, args=None):
        self.args = args
        super().__init__(discord_user_id, self.achievement_name, self.achievement_description,
             self.score_total, self._score, db_client
        )


    def _score(self):
        self.score_current += 1


class BeastMaster(Achievement):
    """
    Beast master achievement. Triggered
    when user sends a message to a specific channel

    Parameters
    ----------

    discord_user_id : int
        Discord user id from user which triggered the achievement

    db_client : DbClient
        Instance of DbClient class

    args : list [Optional]
        List of additional args
    """

    score_total = 1
    achievement_name = 'Beast master'
    achievement_description = 'Prepare for trouble'
    achievement_earning = 'Earned by sending messages at pokemon text channels'
    
    def __init__(self, discord_user_id, db_client, args=None):
        self.args = args
        super().__init__(discord_user_id, self.achievement_name, self.achievement_description,
             self.score_total, self._score, db_client
        )

    def verify(self):
        config = self.args[0]
        message = self.args[1]
        if message.channel.id == config.get_attr('custom', 'pokemon_channel'):
            return True
        return False

    def _score(self):
        if self.verify():
            self.score_current += 1


class AncientKnowledge(Achievement):
    """
    Ancient knowledge achievement. Triggered when
    user uses !diegao or !kdgauga commands anywhere.

    Parameters
    ----------

    discord_user_id : int
        Discord user id from user which triggered the achievement

    db_client : DbClient
        Instance of DbClient class

    args : list [Optional]
        List of additional args
    """

    score_total = 1
    achievement_name = 'Ancient knowledge'
    achievement_description = 'No harm ever came from reading a book.'
    achievement_earning = 'Earned by using !kdgauga or !diegao commands'
    
    def __init__(self, discord_user_id, db_client, args=None):
        self.args = args
        super().__init__(discord_user_id, self.achievement_name, self.achievement_description,
             self.score_total, self._score, db_client
        )

    def verify(self):
        if '!kdgauga' in self.args[0] or '!diegao' in self.args[0]:
            return True
        return False

    def _score(self):
        if self.verify():
            self.score_current += 1
    

class ImARogue(Achievement):
    """
    Im a rouge achievement. Triggered when
    users tried to make bot play music using command >play

    Parameters
    ----------

    discord_user_id : int
        Discord user id from user which triggered the achievement

    db_client : DbClient
        Instance of DbClient class

    args : list [Optional]
        List of additional args
    """

    score_total = 1
    achievement_name = 'I\'m a rogue!!!'
    achievement_description = 'Give me this guitar'
    achievement_earning = 'Earned by asking IwakuraBot to play a song'
    
    def __init__(self, discord_user_id, db_client, args=None):
        self.args = args
        super().__init__(discord_user_id, self.achievement_name, self.achievement_description,
             self.score_total, self._score, db_client
        )


    def _score(self):
        self.score_current += 1


class TheJester(Achievement):
    """
    The jester achievement. Triggered each
    time a menssage is sent with one or more 'k' in it

    Parameters
    ----------

    discord_user_id : int
        Discord user id from user which triggered the achievement

    db_client : DbClient
        Instance of DbClient class

    args : list [Optional]
        List of additional args
    """

    score_total = 10000
    achievement_name = 'The Jester'
    achievement_description = 'We live in a society...'
    achievement_earning = 'Earned by sending 10,000 k within messages'
    
    def __init__(self, discord_user_id, db_client, args=None):
        self.args = args
        super().__init__(discord_user_id, self.achievement_name, self.achievement_description,
             self.score_total, self._score, db_client
        )

    def verify(self):
        if 'k' in self.args.content:
            return True
        return False

    def _score(self):
        self.score_current += self.args.content.count('k')


class LibraryOfAlexandria(Achievement):
    """
    Library of Alexandria achievement. Triggered each
    time a menssage is deleted

    Parameters
    ----------

    discord_user_id : int
        Discord user id from user which triggered the achievement

    db_client : DbClient
        Instance of DbClient class

    args : list [Optional]
        List of additional args
    """

    score_total = 100
    achievement_name = 'Library of Alexandria'
    achievement_description = 'We must burn the books, Montag. All the books'
    achievement_earning = 'Earned by deleting 100 messages'
    
    def __init__(self, discord_user_id, db_client, args=None):
        self.args = args
        super().__init__(discord_user_id, self.achievement_name, self.achievement_description,
             self.score_total, self._score, db_client
        )


    def _score(self):
        self.score_current += 1


class MisleadLatter(Achievement):
    """
    Mislead latter achievement. Triggered each
    time a menssage is deleted

    Parameters
    ----------

    discord_user_id : int
        Discord user id from user which triggered the achievement

    db_client : DbClient
        Instance of DbClient class

    args : list [Optional]
        List of additional args
    """

    score_total = 1
    achievement_name = 'Mislead latter'
    achievement_description = ''
    achievement_earning = 'Earned by deleting a message'
    
    def __init__(self, discord_user_id, db_client, args=None):
        self.args = args
        super().__init__(discord_user_id, self.achievement_name, self.achievement_description,
             self.score_total, self._score, db_client
        )


    def _score(self):
        self.score_current += 1


class TimeTraveler(Achievement):
    """
    Time traveler achievement. Triggered each
    time a menssage is edited

    Parameters
    ----------

    discord_user_id : int
        Discord user id from user which triggered the achievement

    db_client : DbClient
        Instance of DbClient class

    args : list [Optional]
        List of additional args
    """

    score_total = 100
    achievement_name = 'Time traveler'
    achievement_description = 'Yes, and imagine a world where there were no hypothetical situations.'
    achievement_earning = 'Earned by editing 100 messages'
    
    def __init__(self, discord_user_id, db_client, args=None):
        self.args = args
        super().__init__(discord_user_id, self.achievement_name, self.achievement_description,
             self.score_total, self._score, db_client
        )


    def _score(self):
        self.score_current += 1


class Mimic(Achievement):
    """
    Mimic achievement. Triggered each
    time a reaction is added to a message

    Parameters
    ----------

    discord_user_id : int
        Discord user id from user which triggered the achievement

    db_client : DbClient
        Instance of DbClient class

    args : list [Optional]
        List of additional args
    """

    score_total = 69
    achievement_name = 'Mimic'
    achievement_description = '😃😱🤔😢'
    achievement_earning = 'Earned by reacting messages with 69 emojis'
    
    def __init__(self, discord_user_id, db_client, args=None):
        self.args = args
        super().__init__(discord_user_id, self.achievement_name, self.achievement_description,
             self.score_total, self._score, db_client
        )


    def _score(self):
        self.score_current += 1


class YouAreFinallyAwake(Achievement):
    """
    You're finally awake achievement. Triggered when
    a user joins the server.

    Parameters
    ----------

    discord_user_id : int
        Discord user id from user which triggered the achievement

    db_client : DbClient
        Instance of DbClient class

    args : list [Optional]
        List of additional args
    """

    score_total = 1
    achievement_name = 'You\'re finally awake'
    achievement_description = 'You were trying to cross the border, right?'
    achievement_earning = 'Earned by joining the server'
    
    def __init__(self, discord_user_id, db_client, args=None):
        self.args = args
        super().__init__(discord_user_id, self.achievement_name, self.achievement_description,
             self.score_total, self._score, db_client
        )


    def _score(self):
        self.score_current += 1


class WheelOfFortune(Achievement):
    """
    Wheel of fortune achievement. Triggered when
    a message is sent, but it is only score when
    the message contains a random word.

    Parameters
    ----------

    discord_user_id : int
        Discord user id from user which triggered the achievement

    db_client : DbClient
        Instance of DbClient class

    args : list [Optional]
        List of additional args
    """

    score_total = random.randint(10, 100)
    achievement_name = 'Wheel of fortune'
    achievement_description = 'Bow down before the God of Death.'
    achievement_earning = 'It\'s complex, ask for this achievement to an admin'
    
    def __init__(self, discord_user_id, db_client, args=None):
        self.args = args
        super().__init__(discord_user_id, self.achievement_name, self.achievement_description,
            self.score_total, self._score, db_client
        )


    def verify(self):
        chars = 'qwertyuiopasdfghjklçzxcvbnm'
        self._size = random.randint(1, 5)
        _sel_chars = random.choices(chars, k=self._size)
        for _char in _sel_chars:
            if not _char in self.args[0]:
                return False
            return True


    def _score(self):
        if self.verify():
            self.score_current += self._size


class Charge(Achievement):
    """
    Charrrrrrrrrrrge!! achievement. Triggered when
    a message is sent fully uppercase with ten or more
    characters.

    Parameters
    ----------

    discord_user_id : int
        Discord user id from user which triggered the achievement

    db_client : DbClient
        Instance of DbClient class

    args : list [Optional]
        List of additional args
    """

    score_total = 1
    achievement_name = 'Charrrrrrrrrrge!!!!!'
    achievement_description = 'YAAAAARRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR'
    achievement_earning = 'Earned by sending a message fully uppercase with 10+ characters'
    
    def __init__(self, discord_user_id, db_client, args=None):
        self.args = args
        super().__init__(discord_user_id, self.achievement_name, self.achievement_description,
             self.score_total, self._score, db_client
        )

    def verify(self):
        message = self.args
        if len(message.content) >= 10 and message.content.upper() == message.content:
            return True
        return False

    def _score(self):
        if self.verify():
            self.score_current += 1


class MakeItDouble(Achievement):
    """
    Make it double achievement. Triggered when
    kdgauga command returns exactly the double

    Parameters
    ----------

    discord_user_id : int
        Discord user id from user which triggered the achievement

    db_client : DbClient
        Instance of DbClient class

    args : list [Optional]
        List of additional args
    """

    score_total = 1
    achievement_name = 'Make it double'
    achievement_description = 'https://www.youtube.com/watch?v=UQy1bL9WdmY'
    achievement_earning = 'Earned by making Gauga get the double of farm'
    
    def __init__(self, discord_user_id, db_client, args=None):
        self.args = args
        super().__init__(discord_user_id, self.achievement_name, self.achievement_description,
             self.score_total, self._score, db_client
        )


    def _score(self):
        self.score_current += 1


class Lvl20Bard(Achievement):
    """
    Lvl 20 bard achievement. Triggered when
    sending 50 times the commands !play or ~>play

    Parameters
    ----------

    discord_user_id : int
        Discord user id from user which triggered the achievement

    db_client : DbClient
        Instance of DbClient class

    args : list [Optional]
        List of additional args
    """

    score_total = 50
    achievement_name = 'Lvl 20 Bard'
    achievement_description = 'uOOOOOn'
    achievement_earning = 'Earned by using !play or ~>play commands 50 times'
    
    def __init__(self, discord_user_id, db_client, args=None):
        self.args = args
        super().__init__(discord_user_id, self.achievement_name, self.achievement_description,
             self.score_total, self._score, db_client
        )

    def verify(self):
        message = self.args
        if message.content.startswith('!play') or message.content.startswith('~>play'):
            return True
        return False

    def _score(self):
        if self.verify():
            self.score_current += 1


class SOFAMOUS(Achievement):
    """
    SO FAMOUS achievement. earned when
    user gets the role nobility

    Parameters
    ----------

    discord_user_id : int
        Discord user id from user which triggered the achievement

    db_client : DbClient
        Instance of DbClient class

    args : list [Optional]
        List of additional args
    """

    score_total = 1
    achievement_name = 'SO FAMOUS'
    achievement_description = 'Loving you is cherry pie'
    achievement_earning = 'Earned by getting the role Nobility'
    
    def __init__(self, discord_user_id, db_client, args=None):
        self.args = args
        super().__init__(discord_user_id, self.achievement_name, self.achievement_description,
             self.score_total, self._score, db_client
        )

    def verify(self):
        if self.args[0].get_attr('custom', 'nobility') in self.args[1]:
            return True
        return False

    def _score(self):
        if self.verify():
            self.score_current += 1


class MyHouseMyLife(Achievement):
    """
    My house my life achievement. earned when
    user gets the role citizen

    Parameters
    ----------

    discord_user_id : int
        Discord user id from user which triggered the achievement

    db_client : DbClient
        Instance of DbClient class

    args : list [Optional]
        List of additional args
    """

    score_total = 1
    achievement_name = 'My house, my life'
    achievement_description = 'In this world, nothing is certain except death and taxes'
    achievement_earning = 'Earned by getting the role Citizen'
    
    def __init__(self, discord_user_id, db_client, args=None):
        self.args = args
        super().__init__(discord_user_id, self.achievement_name, self.achievement_description,
             self.score_total, self._score, db_client
        )

    def verify(self):
        if self.args[0].get_attr('custom', 'citizen') in self.args[1]:
            return True
        return False

    def _score(self):
        if self.verify():
            self.score_current += 1


class BloodStained(Achievement):
    """
    Blood stained achievement. earned when
    user gets the executioner

    Parameters
    ----------

    discord_user_id : int
        Discord user id from user which triggered the achievement

    db_client : DbClient
        Instance of DbClient class

    args : list [Optional]
        List of additional args
    """

    score_total = 1
    achievement_name = 'Blood steined'
    achievement_description = 'They gonna lose their heads'
    achievement_earning = 'Earned by getting the role Executioner'
    
    def __init__(self, discord_user_id, db_client, args=None):
        self.args = args
        super().__init__(discord_user_id, self.achievement_name, self.achievement_description,
             self.score_total, self._score, db_client
        )

    def verify(self):
        if self.args[0].get_attr('custom', 'executioner') in self.args[1]:
            return True
        return False

    def _score(self):
        if self.verify():
            self.score_current += 1


class Blessed(Achievement):
    """
    Blessed achievement. earned when
    user gets the role clergy

    Parameters
    ----------

    discord_user_id : int
        Discord user id from user which triggered the achievement

    db_client : DbClient
        Instance of DbClient class

    args : list [Optional]
        List of additional args
    """

    score_total = 1
    achievement_name = 'Blessed'
    achievement_description = 'Omenare imperavi emunari'
    achievement_earning = 'Earned by getting the role Clergy'
    
    def __init__(self, discord_user_id, db_client, args=None):
        self.args = args
        super().__init__(discord_user_id, self.achievement_name, self.achievement_description,
             self.score_total, self._score, db_client
        )

    def verify(self):
        if self.args[0].get_attr('custom', 'clergy') in self.args[1]:
            return True
        return False

    def _score(self):
        if self.verify():
            self.score_current += 1


class Congratulations(Achievement):
    """
    Congratulations? achievement. earned when
    user gets the role bunda mole

    Parameters
    ----------

    discord_user_id : int
        Discord user id from user which triggered the achievement

    db_client : DbClient
        Instance of DbClient class

    args : list [Optional]
        List of additional args
    """

    score_total = 1
    achievement_name = 'Congratulations?'
    achievement_description = 'God you\'re pathetic'
    achievement_earning = 'Earned by getting the role Bunda mole'
    
    def __init__(self, discord_user_id, db_client, args=None):
        self.args = args
        super().__init__(discord_user_id, self.achievement_name, self.achievement_description,
             self.score_total, self._score, db_client
        )

    def verify(self):
        if self.args[0].get_attr('custom', 'bunda_mole') in self.args[1]:
            return True
        return False

    def _score(self):
        if self.verify():
            self.score_current += 1


class BrainWashed(Achievement):
    """
    Brain washed achievement. earned when
    user gets the role robot servants

    Parameters
    ----------

    discord_user_id : int
        Discord user id from user which triggered the achievement

    db_client : DbClient
        Instance of DbClient class

    args : list [Optional]
        List of additional args
    """

    score_total = 1
    achievement_name = 'Brain washed'
    achievement_description = 'I need your clothes, your boots, and your motorcycle'
    achievement_earning = 'Earned by getting the role Robot servants'
    
    def __init__(self, discord_user_id, db_client, args=None):
        self.args = args
        super().__init__(discord_user_id, self.achievement_name, self.achievement_description,
             self.score_total, self._score, db_client
        )

    def verify(self):
        if self.args[0].get_attr('custom', 'servant') in self.args[1]:
            return True
        return False

    def _score(self):
        if self.verify():
            self.score_current += 1


class Ni(Achievement):
    """
    Niiiiiii achievement. earned when
    user gets the role knight

    Parameters
    ----------

    discord_user_id : int
        Discord user id from user which triggered the achievement

    db_client : DbClient
        Instance of DbClient class

    args : list [Optional]
        List of additional args
    """

    score_total = 1
    achievement_name = 'Niiiiii'
    achievement_description = 'Niiiiiiiiiiiiiiiiiiiiii'
    achievement_earning = 'Earned by getting the role Knight'
    
    def __init__(self, discord_user_id, db_client, args=None):
        self.args = args
        super().__init__(discord_user_id, self.achievement_name, self.achievement_description,
             self.score_total, self._score, db_client
        )

    def verify(self):
        if self.args[0].get_attr('custom', 'ni') in self.args[1]:
            return True
        return False

    def _score(self):
        if self.verify():
            self.score_current += 1


class UnForastero(Achievement):
    """
    ¡Un forastero! achievement. earned when
    user gets the role subhuman

    Parameters
    ----------

    discord_user_id : int
        Discord user id from user which triggered the achievement

    db_client : DbClient
        Instance of DbClient class

    args : list [Optional]
        List of additional args
    """

    score_total = 1
    achievement_name = '¡Un forastero!'
    achievement_description = 'I could care less what people think'
    achievement_earning = 'Earned by getting the role Subhuman'
    
    def __init__(self, discord_user_id, db_client, args=None):
        self.args = args
        super().__init__(discord_user_id, self.achievement_name, self.achievement_description,
             self.score_total, self._score, db_client
        )

    def verify(self):
        if self.args[0].get_attr('custom', 'subhuman') in self.args[1]:
            return True
        return False

    def _score(self):
        if self.verify():
            self.score_current += 1


class CanineHero(Achievement):
    """
    Canine hero achievement. earned when
    user sends 1k of links

    Parameters
    ----------

    discord_user_id : int
        Discord user id from user which triggered the achievement

    db_client : DbClient
        Instance of DbClient class

    args : list [Optional]
        List of additional args
    """

    score_total = 1000
    achievement_name = 'Canine hero'
    achievement_description = 'I did not ask anything, you fool.. but... t-thanks'
    achievement_earning = 'Earned by sending 1,000 links'
    
    def __init__(self, discord_user_id, db_client, args=None):
        self.args = args
        super().__init__(discord_user_id, self.achievement_name, self.achievement_description,
             self.score_total, self._score, db_client
        )


    def verify(self):
        if re.match(r'https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()@:%_\+.~#?&//=]*)',
             self.args[0]):
            return True
        return False


    def _score(self):
        if self.verify():
            self.score_current += 1


class Heresy(Achievement):
    """
    Heresy achievement. earned when a user leaves the server

    Parameters
    ----------

    discord_user_id : int
        Discord user id from user which triggered the achievement

    db_client : DbClient
        Instance of DbClient class

    args : list [Optional]
        List of additional args
    """

    score_total = 1
    achievement_name = 'Heresy'
    achievement_description = 'Shame. shame. shame. shame. shame.'
    
    def __init__(self, discord_user_id, db_client, args=None):
        self.args = args
        super().__init__(discord_user_id, self.achievement_name, self.achievement_description,
             self.score_total, self._score, db_client
        )

    def _score(self):
        self.score_current += 1


class BurnTheImpostor(Achievement):
    """
    Burn the impostor achievement. earned when a user 
    change its nickname to IwakuraBot

    Parameters
    ----------

    discord_user_id : int
        Discord user id from user which triggered the achievement

    db_client : DbClient
        Instance of DbClient class

    args : list [Optional]
        List of additional args
    """

    score_total = 1
    achievement_name = 'Burn the impostor'
    achievement_description = 'I\'M THE REAL ONE!! DON\'T TRUST HIM!!!'
    achievement_earning = 'Earned by change your nickname to IwakuraBot'
    
    def __init__(self, discord_user_id, db_client, args=None):
        self.args = args
        super().__init__(discord_user_id, self.achievement_name, self.achievement_description,
             self.score_total, self._score, db_client
        )


    def verify(self):
        if self.args[0] == 'IwakuraBot':
            return True
        return False


    def _score(self):
        if self.verify():
            self.score_current += 1


class LeaveTheDoorOpen(Achievement):
    """
    Leave the door open achievement. earned when a user 
    gains the role pesant

    Parameters
    ----------

    discord_user_id : int
        Discord user id from user which triggered the achievement

    db_client : DbClient
        Instance of DbClient class

    args : list [Optional]
        List of additional args
    """

    score_total = 1
    achievement_name = 'Leave the door open'
    achievement_description = 'There are people who come to stay, There are people who go to never again'
    achievement_earning = 'Earned by getting the role Pesant'
    
    def __init__(self, discord_user_id, db_client, args=None):
        self.args = args
        super().__init__(discord_user_id, self.achievement_name, self.achievement_description,
             self.score_total, self._score, db_client
        )

    def verify(self):
        if self.args[0].get_attr('custom', 'pesant') in self.args[1]:
            return True
        return False

    def _score(self):
        if self.verify():
            self.score_current += 1


class HappyHour(Achievement):
    """
    Happy hour achievement. earned when a user joins the voice chat

    Parameters
    ----------

    discord_user_id : int
        Discord user id from user which triggered the achievement

    db_client : DbClient
        Instance of DbClient class

    args : list [Optional]
        List of additional args
    """

    score_total = 1
    achievement_name = 'Happy hour'
    achievement_description = 'On victory, you deserve beer, in defeat, you need it.'
    achievement_earning = 'Earned by joining the voice chat channel'
    
    def __init__(self, discord_user_id, db_client, args=None):
        self.args = args
        super().__init__(discord_user_id, self.achievement_name, self.achievement_description,
             self.score_total, self._score, db_client
        )

    def _score(self):
        self.score_current += 1


class TheRuler(Achievement):
    """
    The Ruler achievement. earned when a earns the role 'Keepers of order'

    Parameters
    ----------

    discord_user_id : int
        Discord user id from user which triggered the achievement

    db_client : DbClient
        Instance of DbClient class

    args : list [Optional]
        List of additional args
    """

    score_total = 1
    achievement_name = 'The Ruler'
    achievement_description = 'Well, I didn’t vote for you'
    achievement_earning = 'Earned by getting the role Keer of orders'
    
    def __init__(self, discord_user_id, db_client, args=None):
        self.args = args
        super().__init__(discord_user_id, self.achievement_name, self.achievement_description,
             self.score_total, self._score, db_client
        )

    def verify(self):
        if self.args[0].get_attr('custom', 'keeper_of_order') in self.args[1]:
            return True
        return False

    def _score(self):
        if self.verify():
            self.score_current += 1