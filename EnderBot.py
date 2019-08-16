import discord
from discord.ext import commands
import random
import os


bot = commands.Bot ("?")

await bot.change_presence(activity=discord.Game('Watching Pewdiepie'), status='idle')

@bot.event
async def on_ready():
    print("Bot online")


@bot.command()
async def ping(ctx):
    """Pings the bot."""
    embed = discord.Embed(colour=0x00FF00)
    embed.add_field(name="Ping", value=f'🏓 {round(bot.latency * 1000)}ms')
    await ctx.send(embed=embed)



bot.run(os.getenv('TOKEN'))
