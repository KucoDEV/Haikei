import json
from discord.ext import commands
import time
import asyncio

def getConfig(guildID):
    with open("config.json", "r") as config:
        data = json.load(config)
    if str(guildID) not in data["guilds"]:
        defaultConfig = {
            "owner": " ",
            "sanction": "kick",
            "antispam": False,
            "antilink": False,
            "automod": False,
            "join": False,
            "autorole": False
        }
        updateConfig(guildID, defaultConfig)
        return defaultConfig
    return data["guilds"][str(guildID)]


def updateConfig(guildID, data):
    with open("config.json", "r") as config:
        config = json.load(config)
    config["guilds"][str(guildID)] = data
    newdata = json.dumps(config, indent=4, ensure_ascii=False)
    with open("config.json", "w") as config:
        config.write(newdata)


def guild_owner_only():
    async def predicate(ctx):
        return ctx.author == ctx.guild.owner
    return commands.check(predicate)


async def update_data(users, user):
    if not f'{user.id}' in users:
        users[f'{user.id}'] = {}
        users[f'{user.id}']['warns'] = 0