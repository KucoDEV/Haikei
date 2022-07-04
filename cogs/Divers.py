import discord
from discord.ext import commands
import datetime
from pystyle import System
import platform
from discord import *
import datetime
import time
import os
from dislash import slash_command, Option, OptionType

class Divers(commands.Cog):
    def __init__(self, client):
        self.client = client

    @slash_command(description="Montre la latence du bot.")
    async def ping(self, ctx):
        await ctx.send(f"Pong! *{round(self.client.latency * 1000)}ms*")

    @slash_command(description="Montre les informations du serveur.")
    async def serverinfo(self, ctx):
        emote = ("<:fleche:957237102616125450>")
        guild_roles = len(ctx.guild.roles)
        guild_members = len(ctx.guild.members)
        text_channels = len(ctx.guild.text_channels)
        voice_channels = len(ctx.guild.voice_channels)
        channels = text_channels + voice_channels
        serverinfo = discord.Embed(color=discord.Color.from_rgb(255, 0, 60), title="Information du serveur")
        serverinfo.add_field(name="<:note:957232264989802537> » Information :",
                             value=f"**Nom :** {ctx.guild.name}\n"
                                   f"**ID :** {ctx.guild.id}\n"
                                   f"**Region :** {ctx.guild.region}\n"
                                   f"**Creation :** <t:{round(ctx.guild.created_at.timestamp())}:R>\n"
                                   f"**Membres :** {guild_members}\n"
                                   f"**Roles :** {guild_roles}\n"
                                   f"**Salons :** {channels}\n"
                                   f"{emote} **Text :** {text_channels}\n"
                                   f"{emote} **Vocal :** {voice_channels}\n\n"
                                   f"**<:couronne:957232264897495040> » Owner :** \n**Nom :** {ctx.guild.owner.name}\n"
                                   f"**ID :** {ctx.guild.owner.id}\n"
                                   f"**Mention :** {ctx.guild.owner.mention}\n\n", inline=False)
        serverinfo.set_thumbnail(url=ctx.guild.icon_url)
        serverinfo.set_image(url=ctx.guild.banner_url)
        serverinfo.set_footer(text=f"{self.client.user.name} © ・ 2021/2022", icon_url=self.client.user.avatar_url)
        await ctx.send(embed=serverinfo)

    @slash_command(description="Montre les informations d'un membre.")
    async def userinfo(self, ctx, member: discord.Member = None):
        online = ("<:Online:937753219269021717>")
        idle = ("<:Idle:937753219248033812>")
        dnd = ("<:DND:937753219197702164>")
        emote = ("<:fleche:957237102616125450>")
        member = ctx.author if not member else member
        member_roles = len(member.roles)
        info = discord.Embed(title=f"Information sur {member.name}", color=discord.Color.from_rgb(255, 0, 60))
        info.add_field(name=f"<:groupe:957232264641642497> » Information :",
                        value=f"**Nom :** {member.name}\n"
                              f"**Tag :** {member}\n"
                              f"**ID :** {member.id}\n"
                              f"**Mention :** {member.mention}\n"
                              f"**Creation :** <t:{round(member.created_at.timestamp())}:R>\n")
        info.add_field(name="<:ordi:957232265019162644> » Serveur :",
                           value=f"**A rejoint :** <t:{round(member.joined_at.timestamp())}:R>\n**Rôles :** {member_roles}\n**Couleur :** {member.colour}\n**Nickname :** {member.nick if member.nick is not None else 'Aucun'}", inline=False)
        req = await self.client.http.request(discord.http.Route("GET", "/users/{uid}", uid=member.id))
        banner_id = req["banner"]
        if banner_id:
            banner_url = f"https://cdn.discordapp.com/banners/{member.id}/{banner_id}?size=1024"
            info.add_field(name="**――――――――――**", value=f"[Avatar]({member.avatar_url}) | [Banner]({banner_url})")
            info.set_image(url=banner_url)
        else:
            info.add_field(name="**――――――――――**", value=f"[Avatar]({member.avatar_url})")
        info.set_thumbnail(url=member.avatar_url)
        info.set_footer(text=f"{self.client.user.name} © ・ 2021/2022", icon_url=self.client.user.avatar_url)
        await ctx.send(embed=info)

    @slash_command(description="Montre les informations sur un lien.",
        options=[
            Option("invite", "Donnez le lien d'invitation", OptionType.STRING, required=True)
        ]
    )
    async def inviteinfo(self, ctx, invite):
        emote = ("<:fleche:957237102616125450>")
        invite = await self.client.fetch_invite(invite)
        inviteinfo = discord.Embed(color=discord.Color.from_rgb(255, 0, 60), title=f"Invite Info")
        inviteinfo.add_field(name="Information: ",
                             value=f"{emote} **Nom:** {invite.guild.name}\n"
                                   f"{emote} **ID:** {invite.guild.id}\n"
                                   f"{emote} **Creation:** <t:{round(invite.guild.created_at.timestamp())}:R>\n"
                                   f"{emote} **Inviter:** {invite.inviter}\n"
                                   f"{emote} **Membres:** {invite.approximate_member_count}\n"
                                   f"{emote} **Salon:** {invite.channel}\n"
                                   f"{emote} **Utilisation:** {invite.uses}")
        inviteinfo.set_thumbnail(url=invite.guild.icon_url)
        inviteinfo.add_field(name="**――――――――――**", value=f"[Icon]({invite.guild.icon_url}) | [Invite Link]({invite})",
                             inline=False)
        inviteinfo.set_footer(text=f"{self.client.user.name} © ・ 2021/2022", icon_url=self.client.user.avatar_url)
        await ctx.send(embed=inviteinfo)

    @slash_command(description="Signale un problème sur le bot.",
        options=[
            Option("message", "Donnez votre bug", OptionType.STRING, required=True)
        ]
    )
    async def bug(self, ctx, *, message):
        prefix = ("/")
        if message == None:
            await ctx.send(f"Faites `{prefix}bug` pour que la commande fonctionne!")
        else:
            await ctx.send("Merci d'avoir signaler se problème!")

            channel = self.client.get_channel(955140030207238174)
            embed2 = discord.Embed(title=f"Bug trouver par {ctx.author}", color=discord.Color.from_rgb(255, 0, 60))
            embed2.add_field(name="Serveur", value=f"{ctx.guild.name}")
            embed2.add_field(name="Bug", value=f"{message}")
            embed2.set_thumbnail(url=ctx.guild.icon_url)
            embed2.set_footer(text=f"{self.client.user.name} © ・ 2021/2022", icon_url=self.client.user.avatar_url)
            await channel.send(embed=embed2)

def setup(client):
    client.add_cog(Divers(client))