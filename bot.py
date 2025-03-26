import os
import random
import aiohttp
import discord
from discord.ext import commands
from discord import app_commands
from dotenv import load_dotenv
from flask import Flask
from threading import Thread

# Flask web server setup
app = Flask('')

@app.route('/')
def home():
    return "JayBot is alive! 🚀"

def run_web_server():
    app.run(host='0.0.0.0', port=8080)

# Load bot token from .env
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

# Bot setup
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='-', intents=intents)

# Sync slash commands when bot is ready
@bot.event
async def on_ready():
    await bot.tree.sync()
    print(f'✅ Logged in as {bot.user} | Slash commands synced')

# Slash commands below 👇

@bot.tree.command(name="hello", description="Say hello to JayBot")
async def hello_slash(interaction: discord.Interaction):
    await interaction.response.send_message("Hello there! 👋")

@bot.tree.command(name="joke", description="Get a programming joke")
async def joke_slash(interaction: discord.Interaction):
    jokes = [
        "Why don't programmers like nature? It has too many bugs.",
        "Why do Java developers wear glasses? Because they don't C#.",
        "How many programmers does it take to change a light bulb? None — it’s a hardware problem."
    ]
    await interaction.response.send_message(random.choice(jokes))

@bot.tree.command(name="flip", description="Flip a coin")
async def flip_slash(interaction: discord.Interaction):
    result = random.choice(["Heads 🪙", "Tails 🪙"])
    await interaction.response.send_message(f"The coin landed on: {result}")

@bot.tree.command(name="roll", description="Roll a 6-sided die")
async def roll_slash(interaction: discord.Interaction):
    result = random.randint(1, 6)
    await interaction.response.send_message(f"You rolled a 🎲 {result}!")

@bot.tree.command(name="8ball", description="Ask the magic 8-ball a question")
async def eight_ball_slash(interaction: discord.Interaction):
    responses = [
        "It is certain.",
        "Reply hazy, try again.",
        "Don't count on it.",
        "Yes, definitely!",
        "Ask again later.",
        "Very doubtful."
    ]
    await interaction.response.send_message(f"🎱 {random.choice(responses)}")

@bot.tree.command(name="menu", description="Show all available commands")
async def menu_slash(interaction: discord.Interaction):
    commands_list = """
🧾 **JayBot Menu**:
`/hello` – Say hello  
`/meme` – Get a random meme  
`/physics` – Learn Physics from Prof  
`/joke` – Get a programming joke  
`/flip` – Flip a coin  
`/roll` – Roll a dice  
`/8ball` – Ask the magic 8-ball  
`/menu` – Show this menu
"""
    await interaction.response.send_message(commands_list)

@bot.tree.command(name="meme", description="Get a random meme")
async def meme_slash(interaction: discord.Interaction):
    async with aiohttp.ClientSession() as session:
        async with session.get("https://meme-api.com/gimme") as response:
            if response.status == 200:
                data = await response.json()
                meme_title = data["title"]
                meme_url = data["url"]
                await interaction.response.send_message(f"**{meme_title}**\n{meme_url}")
            else:
                await interaction.response.send_message("Could not fetch a meme 😢")

@bot.tree.command(name="physics", description="Get a random physics fact")
async def physics_slash(interaction: discord.Interaction):
    facts = [
        "Light behaves as both a particle and a wave. 🌊💡",
        "The speed of light is approximately 299,792,458 meters per second. ⚡",
        "A teaspoon of a neutron star would weigh about 6 billion tons. ☄️",
        "Gravity is the weakest of the four fundamental forces — but it has infinite range! 🪐",
        "Time moves slower the closer you are to a massive object. ⏳",
        "Absolute zero is -273.15°C — the point where atoms stop moving. 🧊",
        "Black holes can warp space and time so much, time almost stops near them. 🕳️",
        "Your mass doesn’t change in space — your *weight* does. 🧑‍🚀",
        "If the sun were replaced with a black hole of the same mass, Earth would keep orbiting normally — but it'd be *very* dark. ☀️➡️🕳️",
        "Quantum rules small things.",
        "Electrics and magnets link.",
        "Heat is energy flow.",
        "Sound is a wave.",
        "Nuclei hold protons, neutrons.",
        "Dark matter is unseen.",
        "Stars fuse atoms.",
        "Entropy increases disorder.",
        "The weak force decays atoms.",
        "Physics describes the universe."
    ]
    await interaction.response.send_message(random.choice(facts))

# Start Flask + Bot
if __name__ == "__main__":
    Thread(target=run_web_server).start()
    bot.run(TOKEN)
