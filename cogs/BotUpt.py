import discord
from discord.ext import commands
from dislash import slash_command
import datetime

starttime = datetime.datetime.utcnow()

class BotUpt(commands.Cog):
    def __init__(self, client):
        self.client = client

    @slash_command(description="Montre depuis combien de temps le bot est en ligne.")
    async def uptime(self, ctx):
        uptime = datetime.datetime.utcnow() - starttime
        uptime = str(uptime).split('.')[0]
        embed = discord.Embed(title=f"{self.client.user} est en ligne depuis :", description=f"```{uptime}```", color=discord.Color.from_rgb(255, 0, 60))
        embed.set_footer(text=f"{self.client.user.name} © ・ 2021/2022", icon_url=self.client.user.avatar_url)
        await ctx.send(embed=embed)

    @slash_command(description="Montre les informations du bot.")
    async def botinfo(self, ctx):
        serverCount = len(self.client.guilds)
        userCount = len(self.client.users)
        uptime = datetime.datetime.utcnow() - starttime
        uptime = str(uptime).split('.')[0]
        bot = discord.Embed(title="Information sur le bot", color=discord.Color.from_rgb(255, 0, 60), description=f"**<:groupe:957232264641642497> » Identité :**\n**Nom :** {self.client.user.mention} `{self.client.user}`\n**ID :** {self.client.user.id}\n**Date de création :** <t:{round(self.client.user.created_at.timestamp())}:R>\n\n**<:dev:957232265270820894> » Developpeur :**\n**Nom :** <@484759949566803979> `> βƗŁŁ#5103`\n**ID :** 484759949566803979\n\n**<:ordi:957232265019162644> » Statistiques :**\n**Utilisateurs :** {userCount}\n**Serveurs :** {serverCount}\n**Ping :** {round(self.client.latency * 1000)}ms\n**Uptime :** {uptime}")
        bot.set_thumbnail(url=self.client.user.avatar_url)
        bot.set_footer(text=f"{self.client.user.name} © ・ 2021/2022", icon_url=self.client.user.avatar_url)
        await ctx.send(embed=bot)

def setup(client):
    client.add_cog(BotUpt(client))