import discord
from discord.ext import commands
from datetime import datetime
from Tools.utils import getConfig, updateConfig
import json
import dislash
from dislash import slash_command, Option, OptionType

class Admin(commands.Cog):
    def __init__(self, client):
        self.client = client


    @slash_command(description="Affiche la configuration du serveur.")
    @dislash.has_permissions(administrator=True)
    async def settings(self, ctx):
        data = getConfig(ctx.guild.id)
        automod = data["automod"]
        antispam = data["antispam"]
        antilink = data["antilink"]
        join = data["join"]
        autorole = data["autorole"]
        if automod is True:
            embed = discord.Embed(description=f"** Administration  ・  /set**\n> `Auto-Mode`・{'<:on:957595187377492038>' if automod is True else '<:off:957595187507519608>'}\n> `Anti-Spam`・{'<:on:957595187377492038>' if antispam is True else '<:off:957595187507519608>'}\n> `Anti-Link`・{'<:on:957595187377492038>' if antilink is True else '<:off:957595187507519608>'}\n\n** Accueil  ・  /config**\n> `Salon`・{f'<#{join}>' if join is not False else f'<:off:957595187507519608>'}\n> `AutoRole`・{f'<@&{autorole}>' if autorole is not False else '<:off:957595187507519608>'}", color=discord.Color.from_rgb(255, 0, 60))
            embed.set_author(name=f"Paramètres de {self.client.user.name}", icon_url=self.client.user.avatar_url)
            embed.set_footer(text=f"{self.client.user.name} © ・ 2021/2022", icon_url=self.client.user.avatar_url)
            await ctx.send(embed=embed)
        elif automod is False:
            embed = discord.Embed(description=f"** Administration  ・  /set**\n> `Auto-Mode`・{'<:on:957595187377492038>' if automod is True else '<:off:957595187507519608>'}\n\n** Accueil  ・  /config**\n> `Salon`・{f'<#{join}>' if join is not False else f'<:off:957595187507519608>'}\n> `AutoRole`・{f'<@&{autorole}>' if autorole is not False else '<:off:957595187507519608>'}", color=discord.Color.from_rgb(255, 0, 60))
            embed.set_author(name=f"Paramètres de {self.client.user.name}", icon_url=self.client.user.avatar_url)
            embed.set_footer(text=f"{self.client.user.name} © ・ 2021/2022", icon_url=self.client.user.avatar_url)
            await ctx.send(embed=embed)

    
    @slash_command(description="Permet de configurer les msg de bienvenue.",
        options=[
            Option("option", "join | autorole", OptionType.STRING, required=True),
            Option("statut", "id | off", OptionType.STRING, required=True)
        ]
    )
    async def config(self, ctx, option, statut):
        data = getConfig(ctx.guild.id)
        if option == "join":
            if statut != "on" and statut != "off":
                data["join"] = statut
                updateConfig(ctx.guild.id, data)
                await ctx.send(f"Je viens d'activer les **messages de bienvenue** dans le salon <#{statut}>.")
            elif statut == "off":
                data["join"] = False
                updateConfig(ctx.guild.id, data)
                await ctx.send(f"Je viens de désactiver les **messages de bienvenue**.")
        if option == "autorole":
            if statut != "on" and statut != "off":
                data["autorole"] = statut
                updateConfig(ctx.guild.id, data)
                await ctx.send(f"Je viens d'activer l'**Auto-Rôle** avec le rôle <@&{statut}>.")
            elif statut == "off":
                data["autorole"] = False
                updateConfig(ctx.guild.id, data)
                await ctx.send(f"Je viens de désactiver l'**Auto-Rôle**.")

    
    @slash_command(description="Permet de configurer le serveur.",
        options=[
            Option("option", "antispam | antilink | automod", OptionType.STRING, required=True),
            Option("statut", "on | off", OptionType.STRING, required=True)
        ]
    )
    async def set(self, ctx, option, statut):
        data = getConfig(ctx.guild.id)
        if option == "antispam":
            if statut == "on":
                data["antispam"] = True
                updateConfig(ctx.guild.id, data)
                await ctx.send("Je viens d'activer l'**Anti-Spam**.")
            elif statut == "off":
                data["antispam"] = False
                updateConfig(ctx.guild.id, data)
                await ctx.send("Je viens de désactiver l'**Anti-Spam**.")
        
        elif option == "antilink":
            if statut == "on":
                data["antilink"] = True
                updateConfig(ctx.guild.id, data)
                await ctx.send("Je viens d'activer l'**Anti-Link**.")
            elif statut == "off":
                data["antilink"] = False
                updateConfig(ctx.guild.id, data)
                await ctx.send("Je viens de désactiver l'**Anti-Link**.")
    
        elif option == "automod":
            if statut == "on":
                data["automod"] = True
                updateConfig(ctx.guild.id, data)
                await ctx.send("Je viens d'activer l'**Auto-Modération**.")
            elif statut == "off":
                data["automod"] = False
                updateConfig(ctx.guild.id, data)
                await ctx.send("Je viens de désactiver l'**Auto-Modération**.")

        else:
            await ctx.send("Je ne trouve pas cette option de sécurité dans ma base de donnée !\n**Options :** `antispam`, `antilink`, `automod`")

    @commands.Cog.listener()
    async def on_message(self, message):
        try:
            try:
                data = getConfig(message.guild.id)
                if data["automod"] is True:
                    if message.content == "" and len(message.attachments) == 0:
                        return
                    try:
                        data = getConfig(message.guild.id)
                        antiSpam = data["antispam"]
                        antiLink = data["antilink"]

                    except AttributeError:
                        pass
                    try:
                        if antiSpam is True:
                            def check(message):
                                return(message.author == message.author and (datetime.utcnow() - message.created_at).seconds < 15)

                            if message.author.guild_permissions.administrator:
                                return

                            if len(list(filter(lambda m: check(m), self.client.cached_messages))) >= 4 and len(list(filter(lambda m: check(m), self.client.cached_messages))) < 8:
                                pass
                            elif len(list(filter(lambda m: check(m), self.client.cached_messages))) >= 8:
                                if data["sanction"] == "kick":
                                    await message.author.kick(reason=f"Auto-Mod | Spam")
                                    channel = self.client.get_channel(955140030207238174)
                                    logs = discord.Embed(title=f"Report Automatique de {message.author}", description=f"> **{message.author.name}** est suspecté d'être un spammer, voici quelques informations supplémentaire :", color=discord.Color.from_rgb(255, 0, 60))
                                    logs.add_field(name="<:server:957579656331132968> » Serveur :", value=f"{message.guild.name}", inline=False)
                                    logs.add_field(name="<:groupe:957232264641642497> » Membre :", value=f"{message.author.name}", inline=False)
                                    logs.add_field(name="<:mod:957579204344565786> » Action :", value=f"Envoie de lien", inline=False)
                                    logs.set_footer(text=f"{self.client.user.name} © ・ 2021/2022", icon_url=self.client.user.avatar_url)
                                    logs.set_thumbnail(url=message.guild.icon_url)
                                    await channel.send(embed=logs)

                        if antiLink is True:
                            if message.author.guild_permissions.administrator:
                                return
                            
                            if "https://" in message.content:
                                await message.delete()

                                if data["sanction"] == "kick":
                                    reason = "Envoie d'un' lien"
                                    await message.author.kick(reason=f"Auto-Mod | {reason}")
                                    channel = self.client.get_channel(955140030207238174)
                                    logs = discord.Embed(title=f"Report Automatique de {message.author}", description=f"> **{message.author.name}** est suspecté d'envoyer des liens, voici quelques informations supplémentaire :", color=discord.Color.from_rgb(255, 0, 60))
                                    logs.add_field(name="<:server:957579656331132968> » Serveur :", value=f"{message.guild.name}", inline=False)
                                    logs.add_field(name="<:groupe:957232264641642497> » Membre :", value=f"{message.author.name}", inline=False)
                                    logs.add_field(name="<:mod:957579204344565786> » Action :", value=f"Envoie d'un' lien", inline=False)
                                    logs.set_footer(text=f"{self.client.user.name} © ・ 2021/2022", icon_url=self.client.user.avatar_url)
                                    logs.set_thumbnail(url=message.guild.icon_url)
                                    await channel.send(embed=logs)

                    except UnboundLocalError:
                        pass
            except AttributeError:
                pass

        except discord.errors.NotFound:
            pass

def setup(client):
    client.add_cog(Admin(client))