import discord
from discord.ext import commands, tasks
from discord.ext.commands import when_mentioned_or
import random
import asyncio
import os

bot = commands.Bot(when_mentioned_or("?"))

@bot.event
async def on_ready():
    print("--------------------")
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('--------------------')
    return

bot.remove_command('help')

@bot.command()
async def ping(ctx):
    """Pings the bot."""
    embed = discord.Embed(colour=0x00FF00)
    embed.add_field(name="Ping", value=f'🏓 {round(bot.latency * 1000 / 2)}ms')
    embed.set_footer(text=f"Request by {ctx.author}", icon_url=ctx.author.avatar_url)
    await ctx.send(embed=embed)

    
@bot.command()
@commands.has_role(567737541546082304)
async def ban(ctx, member: discord.Member, *, reason='No reason provided.'):
    dm = discord.Embed(title="You have been banned from `Ender Network`!", color=0xFF0000)
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
    dm = discord.Embed(title="You have been kicked from `Ender Network`!", color=0xFF0000)
    dm.set_thumbnail(url=member.avatar_url)
    dm.add_field(name="Reason:", value=f"{reason}")
    dm.add_field(name="Moderator:",
                    value=ctx.message.author.display_name)
    await member.send(embed=dm)  # Send DM
    await member.kick(reason=reason)  # Kick
    await ctx.message.delete()  # Delete The Message
    await ctx.send('member has been kicked.')

@bot.command()
async def help(ctx):
    embed = discord.Embed(
        title="Enderbot", description="Moderation Commands:", color=0x00AAFF)
    embed.set_thumbnail(
        url='https://www.emoji.co.uk/files/mozilla-emojis/objects-mozilla/11879-hammer.png')
    embed.add_field(
        name="?kick", value="Kicks a member.", inline=False)
    embed.add_field(
        name="?ban", value="Bans a member.", inline=False)
    embed.add_field(
        name="?clear", value="Clears the amount of messages that you specified in.", inline=False)
    
    await ctx.send(embed=embed)

    otherembed = discord.Embed(
        title="Enderbot", description="Other Commands:", color=0x00AAFF)

    otherembed.set_thumbnail(
        url='https://images.emojiterra.com/twitter/v12/512px/1f3d3.png')
    otherembed.add_field(
        name="?ping", value="Pings the bot.", inline=False)
    otherembed.add_field(
        name="?help", value="Gives this message.", inline=False)
    otherembed.set_footer(
        text=f"Request by {ctx.author}", icon_url=ctx.author.avatar_url)

    await ctx.send(embed=otherembed)

@bot.command()
@commands.has_role(567737541546082304)
async def clear(ctx, amount: int):
    """Clears the amount of messages that you filled in."""
    await ctx.channel.purge(limit=amount + 1)

@clear.error
async def clear_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("You need to specify an amount of messages you want to delete.")
    if isinstance(error, commands.BadArgument):
        await ctx.send("Give an intiger.")

    raise error

async def chng_pr():
    await bot.wait_until_ready()

    await bot.change_presence(activity=discord.Game('with Pewdiepie'))

bot.loop.create_task(chng_pr())
    
bot.run(os.getenv('TOKEN'))
