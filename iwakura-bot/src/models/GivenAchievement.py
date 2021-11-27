"""
Given achievement model.
This class is used to achievements requested by users,
customizable.
"""

import os
from .BaseModel import Achievement

class GivenAchievement(Achievement):
    """
    Given achievement model.
    Mutable achievements, info is given when class
    is instanced. Logo is fixed.
    Also all the achievements created with this
    class ONLY trigger ONCE for completion. This is not mutable.

    Parameter
    ---------

    discord_user_id : int
        Discord user which recieved the achievement

    db_client : DbClient
        DbClient object instance

    achievement_name : str
        name of the achievement

    achievement_description : str
        description of the achievement
    """
    
    score_total = -1
    achievement_earning = 'This is a unique award by members of the server!'

    def __init__(self, discord_user_id, db_client, achievement_name, achievement_description):
        super().__init__(int(discord_user_id), achievement_name, achievement_description,
            self.score_total, self._score, db_client
        )


    def _score(self):
        self.score_current += 1