import os
import random
import aiohttp
from discord.ext import commands
from dotenv import load_dotenv
import discord

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'✅ Logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send("Hello there! 👋")

@bot.command()
async def joke(ctx):
    jokes = [
        "Why don't programmers like nature? It has too many bugs.",
        "Why do Java developers wear glasses? Because they don't C#.",
        "How many programmers does it take to change a light bulb? None — it’s a hardware problem."
    ]
    await ctx.send(random.choice(jokes))

@bot.command()
async def flip(ctx):
    result = random.choice(["Heads 🪙", "Tails 🪙"])
    await ctx.send(f"The coin landed on: {result}")

@bot.command()
async def roll(ctx):
    result = random.randint(1, 6)
    await ctx.send(f"You rolled a 🎲 {result}!")

@bot.command(name="8ball")
async def eight_ball(ctx):
    responses = [
        "It is certain.",
        "Reply hazy, try again.",
        "Don't count on it.",
        "Yes, definitely!",
        "Ask again later.",
        "Very doubtful."
    ]
    await ctx.send(f"🎱 {random.choice(responses)}")

@bot.command()
async def menu(ctx):
    commands_list = """
🧾 **Bot Menu**:
`!hello` – Say hello  
`!meme` – Gives random meme  
`!physics` – Learn Physics from Prof  
`!joke` – Get a random joke  
`!flip` – Flip a coin  
`!roll` – Roll a dice  
`!8ball` – Ask the magic 8-ball  
`!menu` – Show this menu
"""
    await ctx.send(commands_list)

    import aiohttp

@bot.command()
async def meme(ctx):
    async with aiohttp.ClientSession() as session:
        async with session.get("https://meme-api.com/gimme") as response:
            if response.status == 200:
                data = await response.json()
                meme_title = data["title"]
                meme_url = data["url"]
                await ctx.send(f"**{meme_title}**\n{meme_url}")
            else:
                await ctx.send("Could not fetch a meme 😢")

@bot.command()
async def physics(ctx):
    facts = [
        "Light behaves as both a particle and a wave. 🌊💡",
        "The speed of light is approximately 299,792,458 meters per second. ⚡",
        "A teaspoon of a neutron star would weigh about 6 billion tons. ☄️",
        "Gravity is the weakest of the four fundamental forces — but it has infinite range! 🪐",
        "Time moves slower the closer you are to a massive object. ⏳ (Thanks, Einstein!)",
        "Absolute zero is -273.15°C — the point where atoms stop moving. 🧊",
        "Black holes can warp space and time so much, time almost stops near them. 🕳️",
        "Your mass doesn’t change in space — your *weight* does. 🧑‍🚀",
        "If the sun were replaced with a black hole of the same mass, Earth would keep orbiting normally — but it'd be *very* dark. ☀️➡️🕳️",
        "Light's speed is constant.",
        "Gravity attracts mass.",
        "Energy is always conserved.",
        "Atoms have nuclei.",
        "Quantum rules small things.",
        "Relativity bends space-time.",
        "Forces cause motion.",
        "Electrics and magnets link.",
        "Heat is energy flow.",
        "Sound is a wave.",
        "Light is wave and particle.",
        "Nuclei hold protons, neutrons.",
        "Dark matter is unseen.",
        "Stars fuse atoms.",
        "Particles obey the Standard Model.",
        "Entropy increases disorder.",
        "Acoustics studies sound.",
        "Some materials lose resistance.",
        "The strong force binds nuclei.",
        "The weak force decays atoms.",
        "Physics describes the universe.",
    ]
    await ctx.send(random.choice(facts))



bot.run(TOKEN)
