import json
import discord
import time
import asyncio
from dislash import slash_command, Option, OptionType
from discord.ext import commands
import datetime


class Modération(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.last_msg = None
    
    @commands.Cog.listener()
    async def on_message_delete(self, message: discord.Message):
        self.last_msg = message

    @slash_command(description="Retrouve le dernier message supprimer.")
    async def snipe(self, ctx: commands.Context):
        if not self.last_msg:
            await ctx.send("Il n'y a aucun message supprimer !")
            return

        author = self.last_msg.author
        content = self.last_msg.content
        ts = datetime.datetime.utcnow()
        
        embed = discord.Embed(description=f"{content}", color=discord.Color.from_rgb(255, 0, 60), timestamp=datetime.datetime.utcnow())
        embed.set_author(name=f"{author}", icon_url=self.last_msg.author.avatar_url)
        embed.set_footer(text=f"{self.client.user.name} © ・ 2021/2022", icon_url=self.client.user.avatar_url)
        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Modération(client))