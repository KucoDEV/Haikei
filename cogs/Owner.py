import discord
from discord.ext import commands
from dislash import slash_command, Option, OptionType

class Owner(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @slash_command(description="Fait quitter le bot d'un serveur.")
    async def leave(self, ctx, guild_id):
        if ctx.author.id == 484759949566803979 or ctx.author.id == 853063343547875328:
            await ctx.send(f"Je quitte se serveur....")
            await self.client.get_guild(int(guild_id)).leave()

def setup(client):
    client.add_cog(Owner(client))