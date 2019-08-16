import discord
from discord.ext import commands
import random
import os


bot = commands.Bot ("?")

await bot.change_presence(activity=discord.Game('Watching Pewdiepie'), status='idle')

@bot.event
async def on_ready():
    print("--------------------")
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('--------------------')
    return


@bot.command()
async def ping(ctx):
    """Pings the bot."""
    embed = discord.Embed(colour=0x00FF00)
    embed.add_field(name="Ping", value=f'🏓 {round(bot.latency * 1000)}ms')
    await ctx.send(embed=embed)

@bot.command()
@commands.has_role(567737541546082304)
async def ban(ctx, member: discord.Member, *, reason='No reason provided.'):
    dm = discord.Embed(title="You have been banned from `Ender Network`!",
                        description="Details about the ban:", color=embcolor)
    dm.add_field(name="Moderator:",
                    value=ctx.message.author.display_name)
    dm.add_field(name="Reason:", value=f"{reason}")
    dm.set_thumbnail(url=member.avatar_url)
    await member.send(embed=dm)  # Send DM
    await member.ban(reason=reason)  # Ban
    await ctx.message.delete()  # Delete The Message
    await ctx.send('member has been banned.')
    
@bot.command()
@commands.has_role(567737541546082304)
async def kick(ctx, member: discord.Member, *, reason='No reason provided.'):
    dm = discord.Embed(
        color=embcolor, title="You have been kicked from `Ender Network`!")
    dm.set_thumbnail(url=member.avatar_url)
    dm.add_field(name="Reason:", value=f"{reason}")
    dm.add_field(name="Moderator:",
                    value=ctx.message.author.display_name)
    await member.send(embed=dm)  # Send DM
    await member.kick(reason=reason)  # Kick
    await ctx.message.delete()  # Delete The Message
    await ctx.send('member has been kicked.')

bot.run(os.getenv('TOKEN1'))
