from typing import Any
import nextcord
from nextcord.ext import commands

from app.main.handlers.log_handler import LogHandler
from app.main.handlers.config_handler import ConfigHandler
from app.main.classes.api.servers import ServerRequests

config = ConfigHandler()
logger = LogHandler()

api_server = ServerRequests()

discord = config.read_config(section="discord")

OWNER_ID = discord['owner_id']
GUILD_ID = discord['guild_id']
BOT_TOKEN = discord['bot_token']


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

@bot.slash_command(name="listservers", description="List all available servers")
async def list_servers(interaction: nextcord.Interaction):
    """
    List all available servers from Crafty Controller. Sends response as list of Discord embeds.

    Parameters
    ----------
    interaction: Interaction
        The interaction object.
    """
    servers = api_server.get_all_servers()

    embeds = []
    for server in servers:
        embed = nextcord.Embed(title=server['server_name'],
                               description=server['type'],
                               color=nextcord.Color.og_blurple())
        embed.add_field(name="Server ID", value=server['server_id'], inline=False)
        embed.add_field(name="Server IP", value=server['server_ip'], inline=True)
        embed.add_field(name="Server Port", value=server['server_port'], inline=True)
        embed.add_field(name="Created", value=server['created'], inline=False)

        embeds.append(embed)

    await interaction.response.send_message(embeds=embeds)

@bot.slash_command(name="listonline", description="List online servers")
async def list_online(interaction: nextcord.Interaction):
    """
    List all online servers from Crafty Controller. Sends response as Discord embed.

    Parameters
    ----------
    interaction: Interaction
        The interation object.
    """
    await interaction.response.send_message(content="*There are no servers online*")

if __name__ == "__main__":
    bot.run(BOT_TOKEN)