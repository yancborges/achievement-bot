# IwakuraBot / Achievement bot

This code is a discord API bot, which give
achievements to users based on their behavior.
This bot is customizable and open source.                                               \
If you want, you can personalize it to your server :D

## Requeriments

- discordpy (core)
- pymongo   (db connection)
- pillow    (achievement img generation)
- dotenv    (credentials security)

## Setup

After getting your discord bot credentials via discord developr portal,
you need to choose a database. This bot uses *pymongo*, but you can set it
to use any other no-relational database.

Then, you need to create a .env file contaning the following keys:

IWK__API__DISCORD_TOKEN -> Bot credentials                                              \
IWK__API__MONGO_URI     -> Mongo connection string                                      \
IWK__DSC__CMD_PREFIX    -> Prefix for text commands                                     \
IWK__RUN__ENVIRONMENT   -> Database environment (prod, dev, hml, etc)                   \
IWK__CST__ADMIN_ID      -> Your (or any) discord user id.                               \

Values with prefix IWK__ACH__ are images for achievement logos.

## Running

Next, you are ready to run main.py file.                                                \
Bot will automatically connect to all channels
that it were given access to.

For testing, you can send >health to any channel

## Customization

### DB

I used mongo in this project due personal preferences (its free tho).                   \
But you can set it to connect to any other nosql db.                                    \
Every db request runs through db_client.py class. So your db methods can                \
be set there. I GUESS it will work fine if this file is properly done.                  \


*Under development*





 
