

import discord
from discord.ext import commands
from discord.ext.commands import Context
# import os


intents = discord.Intents.default()
intents.message_content = True
intents.members = True


bot = commands.Bot(command_prefix=":", intents=intents)






@bot.event
async def on_ready():
   print("We are online!")




# Required to process user commands only and not process bot's messages DO NOT TAMPER
@bot.event
async def on_message(msg: discord.Message) -> None:
   if msg.author == bot.user or msg.author.bot:
       return
   await bot.process_commands(msg)




# The one and only ping command! (i don't thnk this works)
@bot.command(name="Racially motivated", description="Pong!")
async def ping(ctx):
For i in range(1,1000)
   await ctx.send("LMAO")




@bot.command()
async def repeat(ctx, *, arg):
   await ctx.send(arg)




@bot.command()
async def add(ctx, a: int, b: int):
   await ctx.send("Sum: " + str(a + b))


import typing




@bot.command()
async def bottles(ctx, amount: typing.Optional[int] = 99, *, liquid="age appropriate beverage"):
   await ctx.send(f'{amount} bottles of {liquid} on the wall!')




bot.run("Its a secret")
