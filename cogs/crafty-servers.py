# ------ Libraries ------
from typing import Any
import nextcord
from nextcord.ext import commands

from app.main.handlers.log_handler import LogHandler
from app.main.handlers.config_handler import ConfigHandler
import app.main.helpers.server_helper as sh


# ------ Classes ------
config = ConfigHandler()
logger = LogHandler()


# ------ Variables ------
discord = config.read_config(section="discord")
GUILD_ID = discord['guild_id']


# ------ Discord: Crafty server commands ------
class Servers(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot = bot


    @nextcord.slash_command(name="listservers", description="List all available servers", guild_ids=[GUILD_ID])
    async def list_servers(self, interaction: nextcord.Interaction):
        """
        List all available servers from Crafty Controller. Sends response as list of Discord embeds.

        Parameters
        ----------
        interaction: Interaction
            The interaction object.
        """
        logger.create_log(category="bot", message=f"Slash command: /listservers, was just used by {interaction.user}")
        
        servers = sh.pull_servers()

        if servers:
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
        else:
            await interaction.response.send_message(content="*There are no servers found*")


    @nextcord.slash_command(name="listonline", description="List online servers", guild_ids=[GUILD_ID])
    async def list_online(self, interaction: nextcord.Interaction):
        """
        List all online servers from Crafty Controller. Sends response as Discord embed.

        Parameters
        ----------
        interaction: Interaction
            The interation object.
        """
        logger.create_log(category="bot", message=f"Slash command: /listonline, was just used by {interaction.user}")

        servers = sh.pull_online()
        
        if servers:
            embeds = []
            for server in servers:
                embed = nextcord.Embed(title=server['server_name'],
                                    description=server['type'],
                                    color=nextcord.Color.green())
                embed.add_field(name="Server ID", value=server['server_id'], inline=False)
                embed.add_field(name="Players Online", value=server['online'], inline=True)
                embed.add_field(name="CPU Usage", value=str(server['cpu']), inline=True)
                embed.add_field(name="Memory Usage", value=server['mem'], inline=True)
                embed.add_field(name="Started", value=server['started'], inline=False)

                embeds.append(embed)
            
            await interaction.response.send_message(embeds=embeds)
        else:
            await interaction.response.send_message(content="*There are no servers online*")


def setup(bot):
    bot.add_cog(Servers(bot=bot))