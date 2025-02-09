# 🤖 HAIKEI Discord Bot

## 📜 Description

This project is a Discord bot developed in Python using `discord.py` and `dislash` to provide various features for Discord servers. It allows user management, channel management, and custom commands to enhance the members' experience.

## ⚡ Features

- Administration commands (loading/unloading modules, user management).
- Integrated help system (`/help`, `/aide`).
- Information commands (`/ping`, `/serverinfo`, `/userinfo`).
- Event management (`on_guild_join`, `on_member_join`).
- Logging and tracking of messages.
- Advanced permission management for bot owners.
- Reporting and moderation system.
- Bot uptime tracking (`/uptime`).

## 🛠️ Prerequisites

Make sure you have Python installed on your machine as well as the following modules:

```
pip install discord dislash pystyle rich
```

## 🚀 Installation and Execution

1. Clone this repository or download the files.
2. Add your Discord bot token in `bot.py`.
3. Run the script with the command:
   ```
   python bot.py
   ```
4. Ensure that your bot has the required permissions on the Discord server.

## 🖥️ Modules and Extensions

The bot uses multiple extensions (`cogs`) for modular management:
- `Aide.py`: Help and assistance commands.
- `BotUpt.py`: Uptime and statistics management.
- `Divers.py`: Server and user information.
- `Events.py`: Server and member event management.
- `Owner.py`: Commands exclusive to the bot owner.
- `Snipe.py`: Retrieval of recently deleted messages.
- `logMessage.py`: Logging management system.
- `utils.py`: Utility functions and configuration management.

## ⚠️ Warning

This project is intended for educational purposes and should not be used on production servers without appropriate modifications.

## 📜 License

This project is licensed under the MIT license. You are free to modify and redistribute it.
