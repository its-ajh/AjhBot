import lyricsgenius
import os
import discord
import requests
import random
from discord_slash import SlashCommand, SlashContext
from discord_slash.utils.manage_commands import create_option, create_choice
from discord.ext import commands

bot = commands.Bot(command_prefix='!')
slash = SlashCommand(bot, sync_commands=True)

GENIUS_TOKEN = os.environ.get('GENIUS_ACCESS_TOKEN')

genius = lyricsgenius.Genius("GENIUS_TOKEN")

# deez nuts command

@slash.slash(name="deez", description="just says deez nuts")
async def hello(ctx: SlashContext):
    await ctx.send("deez nuts")

# coin flip command

@slash.slash(name="coinflip", description="flips a coin")
async def coinflip(ctx: SlashContext):
    result = random.choice(["heads", "tails"])
    await ctx.send(f"the coin landed on **{result}**")

# talking ben command
"""
@slash.slash(name="talkingben", description="talk to ben")
             options=[
                 create_option(
                     name="say",
                     description="what you want to say to ben",
                     option_type=4,
                     required=True
                 )
             ])

async def coinflip(ctx: SlashContext):
    result = random.choice(["yes", "no", "eurgh.", "ohohoho!", "na na na na...",])
    await ctx.send(f":telephone: **ben?** {result}")

"""
# number picker command

@slash.slash(name="numberpicker",
             description="picks a random number",
             options=[
                 create_option(
                     name="max",
                     description="maximum number to pick from (default: 1000)",
                     option_type=4,
                     required=True
                 ),
                 create_option(
                     name="min",
                     description="minimum number to pick from (default: 1)",
                     option_type=4,
                     required=False
                 )
             ])
async def picknumber(ctx: SlashContext, max: int, min: int = 1):
    if min > max:
        await ctx.send("the minimum value cannot be greater than the maximum number idiot")
        return
    result = random.randint(min, max)
    await ctx.send(f"the number picked is **{result}**")

# quotes command

@slash.slash(name="quote", description="sends a random quote")
async def quote(ctx: SlashContext):
    response = requests.get("https://zenquotes.io/api/random")
    if response.status_code == 200:
        data = response.json()[0]
        quote = data["q"].lower()
        author = data["a"].lower()
        await ctx.send(f"\"{quote}\" - {author}")
    else:
        await ctx.send("failed to fetch a random quote")

# fact command

@slash.slash(name="fact", description="Shows a random fact")
async def fact(ctx: SlashContext):
    response = requests.get("https://uselessfacts.jsph.pl/random.json?language=en")
    if response.status_code == 200:
        data = response.json()
        fact = data["text"].lower()
        await ctx.send(f"{fact}")
    else:
        await ctx.send("Failed to fetch a random fact")

# lyrics command

"""
@slash.slash(name="lyrics",
             description="sends the lyrics of a song",
             options=[
							create_option(
							    name="song",
							    description="name of the song",
							    option_type=3,
							    required=True
							),
							create_option(
							    name="artist",
							    description="name of the artist",
							    option_type=3,
							    required=False
							)
             ])
async def lyrics(ctx: SlashContext, song: str, artist: str):
    # search for the song
    song = genius.search_song(song, artist)
    if song:
        # send the lyrics in lowercase
        await ctx.send(song.lyrics.lower())
    else:
        await ctx.send("couldnt find lyrics 0_0")
"""

# dont edit below

BOT_TOKEN = os.environ.get('DISCORD_BOT_TOKEN')

activity = discord.Activity(type=discord.ActivityType.watching, name="my website")

from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def main():
  return "<h1>bot is up and running</h1>" #Change this if you want

def run():
    app.run(host="0.0.0.0", port=8080) #don't touch this

def keep_alive():
    server = Thread(target=run)
    server.start()
keep_alive()
bot.run(BOT_TOKEN)