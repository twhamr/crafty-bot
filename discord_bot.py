import json
import discord
from discord.ext import commands
from discord import app_commands

GUILD_ID = discord.Object(id=1187561911110336522)

class Client(commands.Bot):
    async def on_ready(self):
        try:
            synced = await self.tree.sync(guild=GUILD_ID)
            print(f"Synced {len(synced)} command(s) to guild {GUILD_ID}")
        except Exception as e:
            print(f"Error syncing commands: {e}")

        print(f"Logged on as {self.user}!")


with open(file="./bot_token.json", mode="r") as file:
    data = json.load(file)
bot_token = data['token']

intents = discord.Intents.default()
intents.message_content = True
client = Client(command_prefix="!", intents=intents)


@client.tree.command(name="hello", description="say Hello!", guild=GUILD_ID)
async def sayHello(interaction: discord.Interaction):
    await interaction.response.send_message("Hello!")

@client.tree.command(name="printer", description="I will print whatever you give me!", guild=GUILD_ID)
async def printer(interaction: discord.Interaction, printer: str):
    await interaction.response.send_message(content=printer)

client.run(bot_token)