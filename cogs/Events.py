import discord
from discord.ext import commands
from discord.utils import get
from pystyle import System
from rich.console import Console
import datetime
from Tools.utils import getConfig

console = Console()
today = datetime.datetime.now()
date_time = today.strftime("%m/%d/%Y, %H:%M:%S")

class Events(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.Cog.listener()
    async def on_ready(self):
        System.Title(f"{self.client.user} - Discord Bot")
        console.print(f"\n[cyan][bold]{self.client.user}[/][/] [white]est connecter au serveur ![/]\n{date_time}\n\n", justify="center")
        await self.client.change_presence(activity=discord.Streaming(name=f"Imagine a bot...", url="https://twitch.tv/nasa"))

    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        membres = len(guild.members)
        channel = self.client.get_channel(955140018140221501)
        text_channels = len(guild.text_channels)
        voice_channels = len(guild.voice_channels)
        channels = text_channels + voice_channels
        embed = discord.Embed(color=discord.Color.from_rgb(255, 0, 60))
        embed.add_field(name=f"{self.client.user.name} vient d'être ajouté au serveur :", value=f"{guild}", inline=False)
        embed.add_field(name="Créateur :", value=f"{guild.owner.mention} **`{guild.owner}`**", inline=False)
        embed.add_field(name="Nombre De Membre :", value=f"{membres}", inline=False)
        embed.add_field(name="Nombre De Salon :", value=f"{channels}", inline=False)
        embed.add_field(name="Création :", value=f"<t:{round(guild.created_at.timestamp())}:R>")
        embed.set_thumbnail(url=guild.icon_url)
        embed.set_footer(text=f"{self.client.user.name} © ・ 2021/2022", icon_url=self.client.user.avatar_url)
        await channel.send(embed=embed)
    

    @commands.Cog.listener()
    async def on_member_join(self, member):
        data = getConfig(member.guild.id)
        autorole = data["autorole"]
        if autorole != False:
            try:
                role = get(member.guild.roles, id=autorole)
                await member.add_roles(role)
            except:
                pass
        

def setup(client):
    client.add_cog(Events(client))