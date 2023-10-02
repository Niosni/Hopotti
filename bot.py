# bot.py
import os
import openai

import discord
from discord.ext import commands
from dotenv import load_dotenv


load_dotenv()
# Discord API key setup
TOKEN = os.getenv('DISCORD_TOKEN')
intents = discord.Intents.all()
client = discord.Client(intents=intents)
bot = commands.Bot(command_prefix='!',intents=intents)

# OpenAI API key setup
openai.api_key = os.getenv("OPENAI_API_KEY")

@bot.command(name='story', help='Tells you a short story')
async def story(ctx):
    prompt_msg = ctx.message[7:]
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=generate_story(prompt_msg),
        temperature=1.1,
        max_tokens=50
    )
    result = response.choices[0].text
    await ctx.send(result)


@bot.command(name='hopo', help='I dare you to try')
@commands.has_role('Admin')
async def hopo(ctx):
    await ctx.send('Ite oot')

@bot.command(name='ask', help='Might provide a good answer')
async def hopo(ctx):
    prompt_msg = ctx.message[5:]
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=generate_weirdness(prompt_msg),
        temperature=1.1,
        max_tokens=50
    )
    result = response.choices[0].text
    await ctx.send(result)

@bot.command(name='ask-really', help='Provides a beautiful answer')
async def hopo(ctx):
    prompt_msg = ctx.message[12:]
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=generate_haiku(prompt_msg),
        temperature=1.1,
        max_tokens=50
    )
    result = response.choices[0].text
    await ctx.send(result)

def generate_weirdness(prompt):
    return """Answer the following question with just a weird answer like the following:
    Question: What is 2+2?
    Answer: Not over 10
    Question: What is the capital of Finland?
    Answer: Turku, or some other finnish city.
    Question: What is water?
    Answer: It's a combination of some stuff. Not dry.
    Question: {}?
    Answer:""".format(prompt)

def generate_haiku(prompt):
    return """Answer the following question with a haiku
    Question: {}?
    Answer:""".format(prompt)

def generate_story(prompt):
    return """Generate a very short story about {}""".format(prompt)

bot.run(TOKEN)