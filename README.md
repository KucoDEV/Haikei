# 🤖 Discord Bot Management System

## 📜 Description

Ce projet est un bot Discord développé en Python utilisant `discord.py` et `dislash` pour offrir diverses fonctionnalités aux serveurs Discord. Il permet la gestion des utilisateurs, des salons, et des commandes personnalisées pour enrichir l'expérience des membres.

## ⚡ Fonctionnalités

- Commandes d'administration (chargement/déchargement de modules, gestion des utilisateurs).
- Système d'aide intégré (`/help`, `/aide`).
- Commandes d'information (`/ping`, `/serverinfo`, `/userinfo`).
- Gestion des événements (`on_guild_join`, `on_member_join`).
- Enregistrement et suivi des logs de messages.
- Gestion des autorisations avancées pour les propriétaires du bot.
- Système de signalement et de modération.
- Suivi du temps de fonctionnement du bot (`/uptime`).

## 🛠️ Prérequis

Assurez-vous d'avoir Python installé sur votre machine ainsi que les modules suivants :

```
pip install discord dislash pystyle rich
```

## 🚀 Installation et exécution

1. Clonez ce repository ou téléchargez les fichiers.
2. Ajoutez votre token bot Discord dans `bot.py`.
3. Exécutez le script avec la commande :
   ```
   python bot.py
   ```
4. Assurez-vous que votre bot dispose des permissions requises sur le serveur Discord.

## 🖥️ Modules et Extensions

Le bot utilise plusieurs extensions (`cogs`) pour une gestion modulaire :
- `Aide.py` : Commandes d'aide et d'assistance.
- `BotUpt.py` : Gestion de l'uptime et des statistiques.
- `Divers.py` : Informations sur le serveur et les utilisateurs.
- `Events.py` : Gestion des événements serveur et membres.
- `Owner.py` : Commandes exclusives au propriétaire du bot.
- `Snipe.py` : Récupération des derniers messages supprimés.
- `logMessage.py` : Système de gestion des logs.
- `utils.py` : Fonctions utilitaires et gestion des configurations.

## ⚠️ Avertissement

Ce projet est destiné à un usage éducatif et ne doit pas être utilisé sur des serveurs en production sans modifications adaptées.

## 📜 Licence

Ce projet est sous licence MIT - voir le fichier LICENSE pour plus de détails.
