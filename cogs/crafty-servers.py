# ------ Libraries ------
import nextcord
from nextcord.ext import commands

from app.main.handlers.log_handler import LogHandler
from app.main.handlers.config_handler import ConfigHandler
import app.main.helpers.server_helper as sh


# ------ Classes ------
config = ConfigHandler()
logger = LogHandler()

class ServerOptions(nextcord.ui.View):
    def __init__(self, server_id: str) -> None:
        super().__init__()
        self.server_id = server_id
        self.value = None

    @nextcord.ui.button(label="Start", style=nextcord.ButtonStyle.green)
    async def start_server(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        self.value = "start_server"
        self.stop()

    @nextcord.ui.button(label="Stop", style=nextcord.ButtonStyle.red)
    async def stop_server(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        self.value = "stop_server"
        self.stop()

    @nextcord.ui.button(label="Restart", style=nextcord.ButtonStyle.blurple)
    async def restart_server(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        self.value = "restart_server"
        self.stop()

class ServerList(nextcord.ui.Select):
    def __init__(self):
        servers = sh.pull_servers()

        select_options = [
            nextcord.SelectOption(label=server['server_name'], value=server['server_id']) for server in servers
        ]

        super().__init__(placeholder="Server Options:", min_values=1, max_values=1, options=select_options)

    async def callback(self, interaction: nextcord.Interaction) -> None:
        view = ServerOptions(server_id=self.values[0])

        await interaction.response.send_message(content="What action would you like to perform: ", view=view)
        await view.wait()

        try:
            sh.send_action(server_id=self.values[0], action=view.value) # type: ignore

            logger.create_log(category="bot", message=f"WARN: action [{view.value}] was just performed on server with ID [{self.values[0]}]")
            await interaction.response.send_message(content="*Action Succeeded*", ephemeral=False)
        except Exception as e:
            logger.create_log(category="bot", message=f"ERROR: result [{e}] for button {view.value}")
            await interaction.response.send_message(content="*Action Failed*")


class ServerDropdown(nextcord.ui.View):
    def __init__(self):
        super().__init__()
        self.add_item(ServerList())

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
        logger.create_log(category="bot", message=f"WARN: Command /listservers, was just used by {interaction.user}")
        
        try:
            servers = sh.pull_servers()

            embeds = []
            for server in servers:
                embed = nextcord.Embed(title=server['server_name'],
                                    description=server['type'],
                                    color=nextcord.Color.og_blurple())
                embed.add_field(name="Server ID", value=server['server_id'], inline=False)
                embed.add_field(name="Created", value=server['created'], inline=False)

                embeds.append(embed)

            await interaction.response.send_message(embeds=embeds)
        except Exception as e:
            logger.create_log(category="bot", message=f"ERROR: result [{e}] for command /listservers")
            await interaction.response.send_message(content="*There are no servers found*")

    @nextcord.slash_command(name="selectserver", description="Provide a dropdown menu to select a server", guild_ids=[GUILD_ID])
    async def select_server(self, interaction: nextcord.Interaction):
        view = ServerDropdown()
        await interaction.response.send_message("Select a server: ", view=view)
        await view.wait()


    @nextcord.slash_command(name="listonline", description="List online servers", guild_ids=[GUILD_ID])
    async def list_online(self, interaction: nextcord.Interaction):
        """
        List all online servers from Crafty Controller. Sends response as Discord embed.

        Parameters
        ----------
        interaction: Interaction
            The interation object.
        """
        logger.create_log(category="bot", message=f"WARN: Command /listonline, was just used by {interaction.user}")

        try:
            servers = sh.pull_online()
        
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
        except Exception as e:
            logger.create_log(category="bot", message=f"ERROR: result [{e}] for command /listonline")
            await interaction.response.send_message(content="*There are no servers online*")


def setup(bot):
    bot.add_cog(Servers(bot=bot))