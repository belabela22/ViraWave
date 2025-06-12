import discord
from discord.ext import commands
import os

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="/", intents=intents)

for file in os.listdir("./commands"):
    if file.endswith(".py"):
        bot.load_extension(f"commands.{file[:-3]}")

@bot.event
async def on_ready():
    print(f"Bot is online as {bot.user}")

bot.run(os.getenv("DISCORD_TOKEN"))
