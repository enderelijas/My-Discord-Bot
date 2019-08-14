import discord
from discord.ext import commands
import random


bot = commands.Bot ("?")

@bot.event
async def on_ready():
    print("Bot online")

await
 bot.change_presence(activity=discord.
Game('Watching Pewdiepie'),
 status='idle')


@bot.command(pass_context=True)
async def ping(ctx):
    await ctx.send("Pong :stuck_out_tongue_closed_eyes: ")



bot.run("NTY1OTUxNDYyNDkzMTI2NjY3.XOmMJA.a4WTS6oh34ppT29-JGtARcfmQM4")
