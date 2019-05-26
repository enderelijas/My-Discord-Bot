import discord
from discord.ext import commands
import random


bot = commands.Bot ("?")

@bot.event
async def on_ready():
    print("Bot online")


@bot.command(pass_context=True)
async def ping(ctx):
    await ctx.send("Pong :stuck_out_tongue_closed_eyes: ")


@bot.command()
async def info(ctx):
    embed = discord.Embed(title="EnderBot",description="Here To make this server a better place!")


bot.run("NTY1OTUxNDYyNDkzMTI2NjY3.XOmMJA.a4WTS6oh34ppT29-JGtARcfmQM4")
