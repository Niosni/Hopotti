# bot.py
import os
import openai

import discord
from discord.ext import commands
from dotenv import load_dotenv
from prompt_generators import *


load_dotenv()
# Discord API key setup
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
GUILD_ADMIN_ID = os.getenv('GUILD_ADMIN_ID')
intents = discord.Intents(messages=True, guilds=True, message_content=True)
client = discord.Client(intents=intents)
bot = commands.Bot(command_prefix='!',intents=intents)
tree = discord.app_commands.CommandTree(client)

# Limits the OpenAI API usage. 
MAX_TOKENS = 100

# OpenAI API key setup
openai.api_key = os.getenv("OPENAI_API_KEY")

@bot.command(name='hopo', help='I dare you to try',guild=discord.Object(id=GUILD))
@commands.has_role('Admin')
async def hopo(ctx):
    await ctx.send('Goofy')

@bot.tree.command(name='askai', description="Ask a question from an AI",guild=discord.Object(id=GUILD))
async def askAI(interaction:discord.Interaction, arg:str):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=arg,
        max_tokens=MAX_TOKENS
    )
    result = response.choices[0].text
    message = f'> {arg}\n{result}'
    await interaction.response.send_message(message)

@bot.tree.command(name="askweird",description="There's something going on",guild=discord.Object(id=GUILD))
async def askweird(interaction:discord.Interaction, arg:str):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=generate_weirdness(arg),
        max_tokens=MAX_TOKENS
    )
    result = response.choices[0].text
    message = f'> {arg}\n{result}'
    await interaction.response.send_message(message)

@bot.tree.command(name="storytime",description="Generate a story from prompt",guild=discord.Object(id=GUILD))
async def storytime(interaction:discord.Interaction, arg:str):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=generate_story(arg),
        max_tokens=MAX_TOKENS
    )
    result = response.choices[0].text
    message = f'> {arg}\n{result}'
    await interaction.response.send_message(message)

@bot.tree.command(name="haiku",description="Generate a haiku from prompt",guild=discord.Object(id=GUILD))
async def haiku(interaction:discord.Interaction, arg:str):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=generate_haiku(arg),
        max_tokens=MAX_TOKENS
    )
    result = response.choices[0].text
    message = f'> {arg}\n{result}'
    await interaction.response.send_message(message)

@bot.tree.command(name="howitsmade",description="How it's made",guild=discord.Object(id=GUILD))
async def howitsmade(interaction:discord.Interaction, arg:str):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=generate_howitsmade(arg),
        max_tokens=MAX_TOKENS
    )
    result = response.choices[0].text
    message = f'> {arg}\n{result}'
    await interaction.response.send_message(message)

@bot.tree.command(name="avatar",description="Get user avatar",guild=discord.Object(id=GUILD))
async def avatar(interaction:discord.Interaction,member:discord.Member):
    await interaction.response.send_message(member.display_avatar)

@bot.tree.command(name='sync', description='OWNER ONLY: Syncs the bot commands on the server',guild=discord.Object(id=GUILD))
async def sync(interaction:discord.Interaction):
    if int(interaction.user.id) == int(GUILD_ADMIN_ID):
        await bot.tree.sync(guild=discord.Object(id=GUILD))
        await interaction.response.send_message('Command tree synced.')
    else:
        await interaction.response.send_message('You must be the owner to use this command!')

@bot.event
async def on_ready():
    print('ready!')

bot.run(TOKEN)