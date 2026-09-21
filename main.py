import os
from threading import Thread
from flask import Flask
import discord
from discord.ext import commands

# Μικρός web server για το Render
app = Flask('')

@app.route('/')
def home():
    return "Bot is running!"

def run_web():
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)

# Εκκίνηση web server σε ξεχωριστό thread
Thread(target=run_web).start()

# Discord Bot
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'Το bot {bot.user} είναι online!')

@bot.command()
async def ping(ctx):
    await ctx.send('Pong! 🏓')

token = os.getenv('DISCORD_TOKEN')
bot.run(token)
