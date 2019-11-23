_version__ = "1.0.2"
from discord import utils, Client
from discord.ext import commands
from discord.utils import find
from cogs.utils import checks, perms
import logging
import random
import os
import typing
import json
import datetime
import aiohttp
import sqlite3
import sys
import traceback
import asyncio
import calendar
import time
from random import randrange



client = commands.bot(command_prefix=".", description="bushibot")

client.remove_command('help')

@client.event
async def on_ready():
    print("bushibot launching")
    game = discord.Game("uwuwuwuwuwuwuw")
    await client.change_presence(status=discord.Status.idle, activity=game)
    print("launched successfully" + client.user.display_name)
    game1 = discord.Game(".help (bushidoe)")
    await client.change_presence(status=discord.Status.online, activity=game1)


@client.command
async def ping(ctx):
    msg = f"Latency is {round(client.latency * 1000)ms}"
    embed = discord.Embed(title="Pong :ping_pong:", description=msg, color=discord.Color.green())
    await ctx.send(embed=embed)
    
    




@client.command()
async def bruh(ctx):
    await ctx.send("bruh")
    

    
@client.command()
async def uwu(ctx):
    await ctx.send("0w0")

@client.command()
async def bean(ctx):
    await ctx.send("Send bean")

@client.command()
async def yeet(ctx):
    await ctx.send("(╯°□°）╯︵ ┻━┻")


@client.command()
async def unyeet(ctx):
    await ctx.send("┬─┬ ノ( ゜-゜ノ)")




@client.command()
async def scream(ctx):
    for i in range(5):
        await ctx.send(f"AAAAAAAAAAAAAAAAAAAAAAAAAA!")


@client.command()
async def reverse(ctx, *, text):
    await ctx.send(text[::-1])


@client.command()
async def shout(ctx, *, text):
    await ctx.send(text.upper())


@client.command()
async def novowels(ctx, *, text):
    vowels = {
        "a": "",
        "e": "",
        "i": "",
        "o": "",
        "u": ""
    }

    new_text = str.maketrans(vowels)
    await ctx.send(text.translate(vowels))


@client.command(aliases=["table"])
async def flip(ctx):
    await ctx.send("```(╯°□°）╯︵ ┻━┻```")


@client.command()
async def poop(ctx):
    msg = """```
    ░░░░░░░░░░░█▀▀░░█░░░░░░
    ░░░░░░▄▀▀▀▀░░░░░█▄▄░░░░
    ░░░░░░█░█░░░░░░░░░░▐░░░
    ░░░░░░▐▐░░░░░░░░░▄░▐░░░
    ░░░░░░█░░░░░░░░▄▀▀░▐░░░
    ░░░░▄▀░░░░░░░░▐░▄▄▀░░░░
    ░░▄▀░░░▐░░░░░█▄▀░▐░░░░░
    ░░█░░░▐░░░░░░░░▄░█░░░░░
    ░░░█▄░░▀▄░░░░▄▀▐░█░░░░░
    ░░░█▐▀▀▀░▀▀▀▀░░▐░█░░░░░
    ░░▐█▐▄░░▀░░░░░░▐░█▄▄░░░
    ░░░▀▀░▄███▄░░░▐▄▄▄▀░░░░```"""
    await ctx.send(msg)


@client.command()
async def rate(ctx, *, thing):
    """ Rates what you desire """
    num = random.randint(0, 100)
    deci = random.randint(0, 9)

    if num == 100:
        deci = 0

    rating = f"{num}.{deci}"
    await ctx.send(f"ID rate {thing} a {rating}/100")


@client.command()
async def storm(ctx):
    await ctx.send("storm discord.py, they can't ban us all")



@client.command()
async def dadjoke(ctx):
    async with aiohttp.ClientSession() as cs:
        async with cs.get('https://icanhazdadjoke.com/', headers={"Accept": "application/json"}) as r:
            res = await r.json()
            await ctx.send(res['joke'])

@client.command()
async def minecraft(ctx):
    await ctx.send("`144.172.70.110` version is `1.12.2`")

@client.command(aliases=['8ball'])
async def eightball(self, ctx, *, _ballInput: str):
    """extra generic just the way you like it"""
    choiceType = random.choice(["(Affirmative)", "(Non-committal)", "(Negative)"])
    if choiceType == "(Affirmative)":
        prediction = random.choice(["It is certain ", 
                                    "It is decidedly so ", 
                                    "Without a doubt ", 
                                    "Yes, definitely ", 
                                    "You may rely on it ", 
                                    "As I see it, yes ",
                                    "Most likely ", 
                                    "Outlook good ", 
                                    "Yes ", 
                                    "Signs point to yes "]) + ":8ball:"

        emb = (discord.Embed(title="Question: {}".format(_ballInput), colour=0x3be801, description=prediction))
    elif choiceType == "(Non-committal)":
        prediction = random.choice(["Reply hazy try again ", 
                                        "Ask again later ", 
                                        "Better not tell you now ", 
                                        "Cannot predict now ", 
                                        "Concentrate and ask again "]) + ":8ball:"
        emb = (discord.Embed(title="Question: {}".format(_ballInput), colour=0xff6600, description=prediction))
    elif choiceType == "(Negative)":
        prediction = random.choice(["Don't count on it ", 
                                        "My reply is no ", 
                                        "My sources say no ", 
                                        "Outlook not so good ", 
                                        "Very doubtful "]) + ":8ball:"
        emb = (discord.Embed(title="Question: {}".format(_ballInput), colour=0xE80303, description=prediction))
    emb.set_author(name='Magic 8 ball', icon_url='https://www.horoscope.com/images-US/games/game-magic-8-ball-no-text.png')
    await ctx.send(embed=emb)
    
@client.command()
async def combine(ctx, name1: str, name2: str):
    name1letters = name1[:round(len(name1) / 2)]
    name2letters = name2[round(len(name2) / 2):]
    join = "".join([name1letters, name2letters])
    emb = (discord.Embed(color=0x36393e, description = f"{join}"))
    emb.set_author(name=f"{name1} + {name2}")
    await ctx.send(embed=emb)

@client.command()
async def poll(self, ctx, *, pollInfo):
    emb = (discord.Embed(description=pollInfo, colour=0x36393e))
    emb.set_author(name=f"Poll by {ctx.message.author}", icon_url="https://lh3.googleusercontent.com/7ITYJK1YP86NRQqnWEATFWdvcGZ6qmPauJqIEEN7Cw48DZk9ghmEz_bJR2ccRw8aWQA=w300")
    try:
        await ctx.message.delete()
    except discord.Forbidden:
            pass
    try:
        pollMessage = await ctx.send(embed=emb)
        await pollMessage.add_reaction("\N{THUMBS UP SIGN}")
        await pollMessage.add_reaction("\N{THUMBS DOWN SIGN}")
    except Exception as e:
        await ctx.send(f"Oops, I couldn't react to the poll. Check that I have permission to add reactions! ```py\n{e}```")
        
client.run(os.getenv('token'))
