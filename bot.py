import discord
from discord.ext import commands
from discord import app_commands

from app.main.handlers.log_handler import LogHandler
from app.main.handlers.config_handler import ConfigHandler
from app.main.classes.api.servers import ServerRequests

config = ConfigHandler()
logger = LogHandler()

server = ServerRequests()

discord_info = config.read_discord()
GUILD_ID = discord.Object(id=discord_info['guild_id'])
BOT_TOKEN = discord_info['bot_token']

class Client(commands.Bot):
    async def on_ready(self):
        try:
            synced = await self.tree.sync(guild=GUILD_ID)
            print(f"Synced {len(synced)} command(s) to guild {GUILD_ID}")
        except Exception as e:
            print(f"Error syncing commands: {e}")

        print(f"Logged on as {self.user}!")


intents = discord.Intents.default()
intents.message_content = True
client = Client(command_prefix="!", intents=intents)


@client.tree.command(name="getallservers", description="Get all server instances from Crafty Controller", guild=GUILD_ID)
async def sayHello(interaction: discord.Interaction):
    all_servers = server.get_all_servers()
    await interaction.response.send_message(content=all_servers)

@client.tree.command(name="printer", description="I will print whatever you give me!", guild=GUILD_ID)
async def printer(interaction: discord.Interaction, printer: str):
    await interaction.response.send_message(content=printer)

client.run(BOT_TOKEN)