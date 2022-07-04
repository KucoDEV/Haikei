from pydoc import describe
import discord
from discord.ext import commands
from pystyle import System
from dislash import slash_command, InteractionClient, SelectMenu, SelectOption

class Aide(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @slash_command(description="Montre le lien d'invitation du bot.")
    async def invite(self, ctx):
        embed = discord.Embed(description=f"[**Cliquer ici pour obtenir le lien pour inviter {self.client.user.name}.**](https://discord.com/oauth2/authorize?client_id={self.client.user.id}&scope=applications.commands+bot&permissions=8)", color=discord.Color.from_rgb(255, 0, 60))
        embed.set_footer(text=f"{self.client.user.name} © ・ 2021/2022", icon_url=self.client.user.avatar_url)
        await ctx.send(embed=embed)
    
    @slash_command(description="Montre toutes les commandes du bot.")
    async def help(self, ctx):
        embed = discord.Embed(title="__Préfix :__  /", description=f"Version du bot `V.1.0`\n\n**<:note:957232264989802537> » Utilitaire**\n> `serverinfo`・Informations sur le serveur\n> `userinfo`・Information sur l'utilisateur\n> `bug`・Signaler un problème sur le bot.\n\n**<:dev:957232265270820894> » Bot**\n> `botinfo`・Information sur le bot\n> `help`・Ouvre ce panel\n> `ping`・Information sur le statut réseau du bot\n> `invite`・Donne le lien d'invitation du bot\n\n**<:couronne:957232264897495040> » Admin  ・  \👷 En développement...**\n> `settings`・Affiche la configuration du serveur\n> `set`・Active ou désactive les différents modules\n\n**<:ordi:957232265019162644> » Racourcis**\n> `help`・aide, cmd\n> `serverinfo`・si\n> `userinfo`・ui\n> `botinfo`・bi\n\n**Je t'invite à regarder ce lien :**\n[Invitation](https://discord.com/oauth2/authorize?client_id={self.client.user.id}&scope=applications.commands+bot&permissions=8)", color=discord.Color.from_rgb(255, 0, 60))
        embed.set_author(name=f"Menu d'aide de {self.client.user.name}", icon_url=self.client.user.avatar_url)
        embed.set_footer(text=f"{self.client.user.name} © ・ 2021/2022", icon_url=self.client.user.avatar_url)
        await ctx.send(embed=embed)
    
    @slash_command(description="Montre toutes les commandes du bot.")
    async def aide(self, ctx):
        embed = discord.Embed(title="__Préfix :__  /", description=f"Version du bot `V.1.0`\n\n**<:note:957232264989802537> » Utilitaire**\n> `serverinfo`・Informations sur le serveur\n> `userinfo`・Information sur l'utilisateur\n> `report`・Signaler un utilisateur\n\n**<:dev:957232265270820894> » Bot**\n> `botinfo`・Information sur le bot\n> `help`・Ouvre ce panel\n> `ping`・Information sur le statut réseau du bot\n> `invite`・Donne le lien d'invitation du bot\n\n**<:couronne:957232264897495040> » Admin  ・  \👷 En développement...**\n> `settings`・Affiche la configuration du serveur\n> `set`・Active ou désactive les différents modules\n\n**<:ordi:957232265019162644> » Racourcis**\n> `help`・aide, cmd\n> `serverinfo`・si\n> `userinfo`・ui\n> `botinfo`・bi\n\n**Je t'invite à regarder ce lien :**\n[Invitation](https://discord.com/oauth2/authorize?client_id={self.client.user.id}&scope=applications.commands+bot&permissions=8)", color=discord.Color.from_rgb(255, 0, 60))
        embed.set_author(name=f"Menu d'aide de {self.client.user.name}", icon_url=self.client.user.avatar_url)
        embed.set_footer(text=f"{self.client.user.name} © ・ 2021/2022", icon_url=self.client.user.avatar_url)
        await ctx.send(embed=embed)
    
    @slash_command(description="Montre toutes les commandes du bot.")
    async def cmd(self, ctx):
        embed = discord.Embed(title="__Préfix :__  /", description=f"Version du bot `V.1.0`\n\n**<:note:957232264989802537> » Utilitaire**\n> `serverinfo`・Informations sur le serveur\n> `userinfo`・Information sur l'utilisateur\n> `report`・Signaler un utilisateur\n\n**<:dev:957232265270820894> » Bot**\n> `botinfo`・Information sur le bot\n> `help`・Ouvre ce panel\n> `ping`・Information sur le statut réseau du bot\n> `invite`・Donne le lien d'invitation du bot\n\n**<:couronne:957232264897495040> » Admin  ・  \👷 En développement...**\n> `settings`・Affiche la configuration du serveur\n> `set`・Active ou désactive les différents modules\n\n**<:ordi:957232265019162644> » Racourcis**\n> `help`・aide, cmd\n> `serverinfo`・si\n> `userinfo`・ui\n> `botinfo`・bi\n\n**Je t'invite à regarder ce lien :**\n[Invitation](https://discord.com/oauth2/authorize?client_id={self.client.user.id}&scope=applications.commands+bot&permissions=8)", color=discord.Color.from_rgb(255, 0, 60))
        embed.set_author(name=f"Menu d'aide de {self.client.user.name}", icon_url=self.client.user.avatar_url)
        embed.set_footer(text=f"{self.client.user.name} © ・ 2021/2022", icon_url=self.client.user.avatar_url)
        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Aide(client))