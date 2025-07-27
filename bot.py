# ------ Libraries ------
from typing import Any
import nextcord
from nextcord.ext import commands
import os

from app.main.handlers.log_handler import LogHandler
from app.main.handlers.config_handler import ConfigHandler
from app.main.api.servers import ServerRequests

# ------ Classes ------
config = ConfigHandler()
logger = LogHandler()
api_server = ServerRequests()

# ------ Variables ------
discord = config.read_config(section="discord")

OWNER_ID = discord['owner_id']
GUILD_ID = discord['guild_id']
BOT_TOKEN = discord['bot_token']

# ------ Discord: Bot Initialization ------
bot = commands.Bot(default_guild_ids=[GUILD_ID], owner_id=OWNER_ID)

@bot.event
async def on_ready():
    """
    Runs setup for Discord Bot
    """
    logger.create_log(category="bot", message=f"Logged in as {bot.user} with owner: {OWNER_ID}")

    try:
        sync_commands = bot.get_all_application_commands()
        await bot.sync_all_application_commands()
        logger.create_log(category="bot", message=f"Synced {len(sync_commands)} command(s) for guild: {GUILD_ID}")
    except:
        logger.create_log(category="bot", message=f"Unable to sync commands")

@bot.slash_command(name="echo", description="Echos the given input")
async def echo(interaction: nextcord.Interaction, arg: str):
    """
    Repeats the message that you send as an argument

    Parameters
    ----------
    interaction: Interaction
        The interaction object.
    arg: str
        The message to repeat. This is a required argument.
    """
    await interaction.response.send_message(content=f"You said: {arg}")

@bot.slash_command(name="hello", description="Says 'Hello World!'")
async def hello(interaction: nextcord.Interaction):
    """
    Simple command that responds with 'Hello World!'

    Parameters
    ----------
    interaction: Interaction
        The interaction object.
    """
    await interaction.response.send_message(content="Hello World!")


if __name__ == "__main__":
    initial_extensions = []

    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            initial_extensions.append("cogs." + filename[:-3])

    bot.load_extensions(names=initial_extensions)

    bot.run(BOT_TOKEN)