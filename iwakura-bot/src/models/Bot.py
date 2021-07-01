import discord
import requests
import inspect
from pymongo import MongoClient
import os
import ssl
import textwrap
import io

from .GivenAchievement import GivenAchievement
from . import BehaviorAchievements
from .db_client import DbClient

from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw 

class Bot:
    """
    """

    ach_classes = BehaviorAchievements
    
    def __init__(self, discord_client, environment, config):
        """
        Creates the instance of main controller.
        This class self handles the biggest part of command
        routines, like connecting to db, manage environment, trigger and
        update achievements.

        Parameters
        ----------

        discord_client : Discord
            instance of discord client class

        environment : str
            environment name, enuns to prod, dev, hml.
            MongoDb tables are used based on this variable
        """
        
        self.discord_client = discord_client
        self.environment = environment
        self.config = config
        self.connect_to_db()


    async def send_notification(self, context, cls):
        """
        Sends a notification to the user when
        a achievement is unlocked

        Parameters
        ----------

        context : discord.message
            discord message class
        
        cls : Achievement
            instance of achievement class which have been
            unlocked
        """
        
        user = await self.discord_client.fetch_user(context)
        msg = self.mount_notication(cls)
        with io.BytesIO() as image_binary:
            msg.save(image_binary, format='PNG')
            image_binary.seek(0)
            await user.send(file=discord.File(fp=image_binary, filename='achievement.png'))
        print('Sent completion notification to', user.id)
        

    async def trigger_achievement(self, context, _class, args=None):
        """
        Triggers an achievement, increases its scores
        and updates into db. It also sends the notification
        if score reaches the total to unlock.

        Parameters
        ----------

        context : discord.message
            discord message class
        
        _class : Achievement
            class that is being triggered

        args : list
            List of optional arguments
        """
        
        send_to = None
        if _class == GivenAchievement:
            cls = GivenAchievement(args[0], self.db_client, args[1], args[2])
            send_to = args[0]
        else:
            cls = _class(context, self.db_client, args=args)
            send_to = context
        
        if not cls.completed:
            cls.score()
            print(f'Triggering {cls.__class__} for user {context}')
            cls.update(self.db_client)

        if cls.completed_by_last_action:
            await self.send_notification(send_to, cls)
            print(f'Completing {cls.__class__} for user {context}')


    async def show_achievements(self, context, target):
        """
        Mounts a message with all unlocked achievements from
        selected user id, and sends to the requester DM.

        Parameters
        ----------

        context : discord.message
            discord message class

        target : int
            target discord user id
        """
        
        _db_unlocked = self.db_client.get('progress', {'discord_user_id': target, 'completed': True})
        db_unlocked = [a for a in _db_unlocked]
        all_achs = {}
        for cls in inspect.getmembers(self.ach_classes):
            _cls_dict = {}
            _cls = inspect.getmembers(cls[1])
            for member in _cls:
                _cls_dict[member[0]] = member[1]
            if 'achievement_name' in _cls_dict:
                all_achs[cls[0]] = (_cls_dict)
                all_achs[cls[0]]["icon_url"] = self.config.get_attr('achievement', cls[0])

        db_unlocked = [ach["achievement_name"] for ach in db_unlocked]
        for cls in all_achs:
            if all_achs[cls]["achievement_name"] in db_unlocked:
                all_achs[cls]["show"] = True
            else:
                all_achs[cls]["show"] = False

        for cls in _db_unlocked:
            if cls["score_total"] == -1:
                cls["show"] = True
                all_achs[cls["achievement_name"]] = cls
        msg = self.mount_image(all_achs)
        with io.BytesIO() as image_binary:
            msg.save(image_binary, format='PNG')
            image_binary.seek(0)
            await context.author.send(file=discord.File(fp=image_binary, filename='achievements.png'))
        print('Sent achievements to', context.author.id)


    def connect_to_db(self):
        """
        Creates a connection to the database and
        to discord API, based on previously loaded
        .env values
        """
        
        MONGO_URI = self.config.get_attr('api', 'mongo_uri')
        client_mongo = MongoClient(MONGO_URI, connect=False, ssl=True, ssl_cert_reqs=ssl.CERT_NONE)
        self.db_client = DbClient(client_mongo, "achievement-bot", self.environment)


    def mount_notication(self, achievement):
        """
        Mount achievement completion image.
        WARNING: THIS IS VERY BAD DONE, SORRY.

        Parameters
        ----------

        achievement : Achievement
            instance of Achievement class
        """
        
        # Base coord values
        x_max = 400
        y_max = 140
        x_logo = 10
        y_logo = 10
        x_title = 120
        y_title = 45
        x_desc = 120
        y_desc = 65
        x_ann = 120
        y_ann = 10
        x_foot = 80
        y_foot = 120
        ach = achievement.to_json()

        # Base empty image
        new_im = Image.new('RGB', (x_max, y_max))
        im = Image.open(requests.get(ach["icon_url"], stream=True).raw)

        # Inserting achievement logo into empty image
        new_im.paste(im, (x_logo,y_logo), im)
        
        # Instancing fonts
        title_font = ImageFont.truetype("arial.ttf", 18)
        desc_font = ImageFont.truetype("arial.ttf", 14)
        foot_font = ImageFont.truetype("arial.ttf", 12)

        def write_lines(text, font, img, x, y, color):
            lines = textwrap.wrap(text, width=30)
            y_text = 0
            for line in lines:
                width, height = font.getsize(line)
                img.text((x, y + y_text),line,color,font=font)
                y_text += 15
        
        # Writing texts
        text_im = ImageDraw.Draw(new_im)
        write_lines('Congratulations! You have unlocked:', desc_font, text_im, x_ann, y_ann, (255,255,255))
        write_lines(ach["achievement_name"], title_font, text_im, x_title, y_title, (255,255,255))
        write_lines(ach["achievement_description"], desc_font, text_im, x_desc, y_desc, (135,135,135))
        text_im.text((x_foot, y_foot),'You can unlock more by interacting at the server!',(0, 202, 224),font=foot_font)

        return new_im


    def mount_image(self, achievements):
        """
        Mounts the image with all locked and unlocked achievements.
        WARNING: THIS IS VERY BAD DONE, SORRY.

        Parameters
        ----------

        achievements : list
            List of all achievements dicts
        """
        
        # Initial coord values
        x_start = 10
        y_start = 20
        footer_size = 100
        y_max = 1000 + y_start
        x_max = round((len(achievements) * 100) / (y_max - y_start)) * 410
        new_im = Image.new('RGB', (x_max, y_max + footer_size))
        x_index = x_start
        y_index = y_start

        # Instancing fonts
        title_font = ImageFont.truetype("arial.ttf", 20)
        desc_font = ImageFont.truetype("arial.ttf", 18)

        def write_lines(text, font, img, option, x, y):
            lines = textwrap.wrap(text, width=30)
            y_text = 0
            for line in lines:
                width, height = font.getsize(line)
                if option == 'title':
                    img.text((x, y + y_text),line,(255,255,255),font=font)
                else:
                    img.text((x, y + y_text),line,(135,135,135),font=font)
                y_text += 15

        # Inserting achievement info into
        # empty image
        for _cls in achievements:
            cls = achievements[_cls]
            text_im = ImageDraw.Draw(new_im)
            if not cls['icon_url']:
                continue
            if cls['show']:
                im = Image.open(requests.get(cls['icon_url'], stream=True).raw)
                write_lines(
                    cls["achievement_name"], title_font, text_im, 'title', x_index + 110, y_index + 20
                )
                write_lines(
                    cls["achievement_description"], desc_font, text_im, 'description', x_index + 110, y_index + 40
                )
            else:
                # Loading default image whrn achievement was not
                # unlocked by user.
                im = Image.open(requests.get(
                    self.config.get_attr('achievement', 'QuestionmarksIcon')
                    , stream=True).raw
                )
                text_im.text((x_index + 110, y_index + 20),'LOCKED ACHIEVEMENT',(255,255,255),font=title_font)
                text_im.text((x_index + 110, y_index + 40),'????????????',(135,135,135),font=desc_font)
            
            # Pastes the image and set coords for the next one
            im=Image.eval(im,lambda x: x+(x_index+y_index)/30)
            new_im.paste(im, (x_index,y_index), im)
            y_index += 110
            if y_index >= y_max - 110:
                y_index = y_start
                x_index += 410

        # Getting values to the % footer text
        unlocked = len(
            [key for key in achievements if achievements[key]["show"] and achievements[key]['score_total'] != -1]
        )
        unlockable = len([key for key in achievements if achievements[key]['score_total'] != -1])
        completion = f'Completion: {round((unlocked / unlockable) * 100, 2)}% of achievements unlocked'
        text_im.text((50, y_max + 30), completion,(255,255,255),font=title_font)

        return new_im