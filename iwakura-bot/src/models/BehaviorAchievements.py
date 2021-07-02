"""
Class models for achievements unlocked by user actions.
All achievements inherits BaseModel.Achievement class.
"""

import random
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
    
    def __init__(self, discord_user_id, db_client, args=None):
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

    def __init__(self, discord_user_id, db_client, args=None):
        super().__init__(discord_user_id, self.achievement_name, self.achievement_description,
             self.score_total, self._score, db_client
        )


    def _score(self):
        self.score_current += 1


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
    
    def __init__(self, discord_user_id, db_client, args=None):
        super().__init__(discord_user_id, self.achievement_name, self.achievement_description,
             self.score_total, self._score, db_client
        )


    def _score(self):
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
    
    def __init__(self, discord_user_id, db_client, args=None):
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
    

    def __init__(self, discord_user_id, db_client, args=None):
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
    

    def __init__(self, discord_user_id, db_client, args=None):
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
    
    def __init__(self, discord_user_id, db_client, args=None):
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

    score_total = 1000000000
    achievement_name = 'Pigeon deity'
    achievement_description = 'Pru pru'
    
    def __init__(self, discord_user_id, db_client, args=None):
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
    
    def __init__(self, discord_user_id, db_client, args=None):
        super().__init__(discord_user_id, self.achievement_name, self.achievement_description,
             self.score_total, self._score, db_client
        )


    def _score(self):
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
    
    def __init__(self, discord_user_id, db_client, args=None):
        super().__init__(discord_user_id, self.achievement_name, self.achievement_description,
             self.score_total, self._score, db_client
        )


    def _score(self):
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
    
    def __init__(self, discord_user_id, db_client, args=None):
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
    
    def __init__(self, discord_user_id, db_client, args=None):
        self.args = args
        super().__init__(discord_user_id, self.achievement_name, self.achievement_description,
             self.score_total, self._score, db_client
        )


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

    score_total = 100
    achievement_name = 'Mislead latter'
    achievement_description = ''
    
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
    
    def __init__(self, discord_user_id, db_client, args=None):
        self.args = args
        super().__init__(discord_user_id, self.achievement_name, self.achievement_description,
            self.score_total, self._score, db_client
        )


    def _score(self):
        chars = 'qwertyuiopasdfghjklçzxcvbnm'
        _size = random.randint(1, 5)
        _sel_chars = random.choices(chars, k=_size)
        for _char in _sel_chars:
            if not _char in self.args[0]:
                return
        self.score_current += _size


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
    
    def __init__(self, discord_user_id, db_client, args=None):
        self.args = args
        super().__init__(discord_user_id, self.achievement_name, self.achievement_description,
             self.score_total, self._score, db_client
        )


    def _score(self):
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
    
    def __init__(self, discord_user_id, db_client, args=None):
        self.args = args
        super().__init__(discord_user_id, self.achievement_name, self.achievement_description,
             self.score_total, self._score, db_client
        )


    def _score(self):
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
    
    def __init__(self, discord_user_id, db_client, args=None):
        self.args = args
        super().__init__(discord_user_id, self.achievement_name, self.achievement_description,
             self.score_total, self._score, db_client
        )


    def _score(self):
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
    
    def __init__(self, discord_user_id, db_client, args=None):
        self.args = args
        super().__init__(discord_user_id, self.achievement_name, self.achievement_description,
             self.score_total, self._score, db_client
        )


    def _score(self):
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
    
    def __init__(self, discord_user_id, db_client, args=None):
        self.args = args
        super().__init__(discord_user_id, self.achievement_name, self.achievement_description,
             self.score_total, self._score, db_client
        )


    def _score(self):
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
    
    def __init__(self, discord_user_id, db_client, args=None):
        self.args = args
        super().__init__(discord_user_id, self.achievement_name, self.achievement_description,
             self.score_total, self._score, db_client
        )


    def _score(self):
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
    
    def __init__(self, discord_user_id, db_client, args=None):
        self.args = args
        super().__init__(discord_user_id, self.achievement_name, self.achievement_description,
             self.score_total, self._score, db_client
        )


    def _score(self):
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
    
    def __init__(self, discord_user_id, db_client, args=None):
        self.args = args
        super().__init__(discord_user_id, self.achievement_name, self.achievement_description,
             self.score_total, self._score, db_client
        )


    def _score(self):
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
    
    def __init__(self, discord_user_id, db_client, args=None):
        self.args = args
        super().__init__(discord_user_id, self.achievement_name, self.achievement_description,
             self.score_total, self._score, db_client
        )


    def _score(self):
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
    
    def __init__(self, discord_user_id, db_client, args=None):
        self.args = args
        super().__init__(discord_user_id, self.achievement_name, self.achievement_description,
             self.score_total, self._score, db_client
        )


    def _score(self):
        self.score_current += 1