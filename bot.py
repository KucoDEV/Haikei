# ------------ Modules ------------ #

import discord
from discord.ext import commands
from rich.console import Console
import os
from dislash import InteractionClient
import datetime
import json
from Tools.utils import getConfig, updateConfig

# ------------ Variables ------------ #

intents = discord.Intents.default()
intents.members = True

console = Console()
client = commands.Bot(command_prefix="+", help_command=None, intents=intents)

inter_client = InteractionClient(client, test_guilds=[votre_guid_id])

# ------------ Cogs ------------ #

@client.command()
async def load(ctx, extension):
    if ctx.message.author.id == votre_id or ctx.message.author.id == 2eme_id:
        client.load_extension(f'cogs.{extension}')
        embed = discord.Embed(title="Chargement de module", description=f"Je viens de charger le module {extension} !", colour=discord.Color.from_rgb(0, 255, 0))
        await ctx.send(embed=embed)
        console.print(f"[grey]([/][green]+[/][grey])[/] [cyan]{extension}[/]", justify="center")

@client.command()
async def unload(ctx, extension):
    if ctx.message.author.id == votre_id or ctx.message.author.id == 2eme_id:
        client.unload_extension(f'cogs.{extension}')
        embed = discord.Embed(title="Déchargement de module", description=f"Je viens de décharger le module {extension} !", colour=discord.Color.from_rgb(255, 0, 0))
        await ctx.send(embed=embed)
        console.print(f"[grey]([/][red]-[/][grey])[/] [cyan]{extension}[/]", justify="center")

@client.command()
async def reload(ctx, extension):
    if ctx.message.author.id == votre_id or ctx.message.author.id == 2eme_id:
        client.reload_extension(f'cogs.{extension}')
        embed = discord.Embed(title="Rechargement de module", description=f"Je viens de recharger le module {extension} !", colour=discord.Color.from_rgb(255, 0, 60))
        await ctx.send(embed=embed)
        console.print(f"[grey]([/][cyan]+[/][grey])[/] [cyan]{extension}[/]", justify="center")


for filename in os.listdir('./cogs'):
    if filename.endswith(".py"):
        client.load_extension(f'cogs.{filename[:-3]}')
        console.print(f"[grey]([/][green]+[/][grey])[/] [cyan]{filename[:-3]}[/]", justify="center")

# ------------ Events ------------ #

@client.event
async def on_guild_join(guild):
    data = getConfig(guild.id)
    data["owner"] = guild.owner_id
    updateConfig(guild.id, data)

    bot_entry = await guild.audit_logs(action=discord.AuditLogAction.bot_add).flatten()
    try:
        join = discord.Embed(
            title=f"Merci d'avoir ajouter {client.user.name} sur votre serveur !",
            colour=discord.Color.from_rgb(255, 0, 60),
            description=f"**Quelques informations :**\n"
            f"**{client.user.name}** est encore en version BETA, seuls quelques serveurs partenaires ont la possibilité d'utiliser notre robot."
        )
        await bot_entry[0].user.send(embed=join)
    except discord.errors.Forbidden:
        pass

@client.event
async def on_guild_remove(guild):
    with open("config.json", "r") as f:
        data = json.load(f)

    del data["guilds"][str(guild.id)]

    with open("config.json", "w") as f:
        json.dump(data, f)

# ------------ Lancement ------------ #

client.run("votre_token")

# ------------ Fin Du Bot ------------ #
