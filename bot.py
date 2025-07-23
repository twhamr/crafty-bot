import discord
from discord.ext import commands
from discord import app_commands

from app.main.handlers.log_handler import LogHandler
from app.main.handlers.config_handler import ConfigHandler
from app.main.classes.api.servers import ServerRequests

config = ConfigHandler()
logger = LogHandler()

api_server = ServerRequests()

discord_info = config.read_discord()
GUILD_ID = discord.Object(id=discord_info['guild_id'])
BOT_TOKEN = discord_info['bot_token']

class Client(commands.Bot):
    async def on_ready(self):
        logger.create_log(category="bot", message=f"Logged on as {self.user}!")

        try:
            synced = await self.tree.sync(guild=GUILD_ID)
            logger.create_log(category="bot", message=f"Synced {len(synced)} command(s) to guild {GUILD_ID}")
        except Exception as e:
            logger.create_log(category="bot", message=f"Error syncing commands: {e}")


intents = discord.Intents.default()
intents.message_content = True
client = Client(command_prefix="!", intents=intents)


@client.tree.command(name="listservers", description="List all server instances", guild=GUILD_ID)
async def list_servers(interaction: discord.Interaction):
    all_servers = api_server.get_all_servers()

    embeds = []
    for server in all_servers:
        temp = discord.Embed(title=server['server_name'],
                             description=server['type'],
                             color=discord.Color.og_blurple())
        
        temp.add_field(name="Server ID", value=server['server_id'], inline=False)
        temp.add_field(name="Server IP", value=server['server_ip'], inline=True)
        temp.add_field(name="Server Port", value=server['server_port'], inline=True)
        temp.add_field(name="Created", value=server['created'], inline=False)
        embeds.append(temp)
    
    await interaction.response.send_message(embeds=embeds)
    

@client.tree.command(name="listonline", description="List all online servers", guild=GUILD_ID)
async def list_online(interaction: discord.Interaction):
    all_servers = api_server.get_all_servers()

    await interaction.response.send_message(content="")

@client.tree.command(name="printer", description="I will print whatever you give me!", guild=GUILD_ID)
async def printer(interaction: discord.Interaction, printer: str):
    await interaction.response.send_message(content=printer)


client.run(BOT_TOKEN)