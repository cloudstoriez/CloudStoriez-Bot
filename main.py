import os
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'Το bot {bot.user} είναι online 24/7!')

@bot.command()
async def ping(ctx):
    await ctx.send('Pong! 🏓')

token = os.getenv('DISCORD_TOKEN')
bot.run(token)
