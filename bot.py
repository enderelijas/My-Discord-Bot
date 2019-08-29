import discord
from discord.ext import commands, tasks
from discord.ext.commands import when_mentioned_or
from discord.utils import get
from itertools import cycle
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
async def creeper(ctx):
    await ctx.send('Aww Man!')

@bot.command()
async def party(ctx):
    embed = discord.Embed(color=0xD5D5D5)
    embed.set_image(url='https://i.redd.it/v16fke5bd32z.gif')
    await ctx.send(embed=embed)

@bot.command()
async def yoshi(ctx):
    embed = discord.Embed(color=0xD5D5D5)
    embed.set_image(url='https://i.kym-cdn.com/photos/images/original/001/417/391/51f.gif')
    await ctx.send(embed=embed)
    await ctx.send('**__SO PHAT__**')
 
@bot.command()
async def ping(ctx):
    embed = discord.Embed(colour=0x00FF00)
    embed.add_field(name="Ping", value=f'🏓 {round(bot.latency * 1000 / 2)}ms')
    embed.set_footer(text=f"Request by {ctx.author}", icon_url=ctx.author.avatar_url)
    await ctx.send(embed=embed)
    
@bot.command()
#@commands.has_role(606479631909912578)
async def ban(ctx, member: discord.Member, *, reason='No reason provided.'):
    dm = discord.Embed(title="You have been banned from `Ender Network`!", color=0xAA00FF)
    dm.add_field(name="Moderator:",
                    value=ctx.message.author.display_name)
    dm.add_field(name="Reason:", value=f"{reason}")
    dm.set_thumbnail(url=member.avatar_url)
    await member.send(embed=dm)  # Send DM
    await member.ban(reason=reason)  # Ban
    await ctx.message.delte()  # Delete The Message
    await ctx.send('member has been banned.')
    
@bot.command()
#@commands.has_role(606479631909912578)
async def kick(ctx, member: discord.Member, *, reason='No reason provided.'):
    dm = discord.Embed(title="You have been kicked from `Ender Network`!", color=0xAA00FF)
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
        title="Enderbot", description="Moderation Commands:", color=0x6D00A3)
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
        title="Enderbot", description="Other Commands:", color=0x570082)

    otherembed.set_thumbnail(
        url='https://images.emojiterra.com/twitter/v12/512px/1f3d3.png')
    otherembed.add_field(name="?ping", value="Pings the bot.", inline=False)
    otherembed.add_field(name="?help", value="Gives this message.", inline=False)
    otherembed.add_field(name="?add", value="Adds 2 numbers.", inline=False)
    otherembed.add_field(name="?multiply", value="Multiply 2 numbers.", inline=False)
    otherembed.add_field(name="?creeper", value="Aww Man!", inline=False)
    otherembed.add_field(name="?yoshi", value="Displays a phat yoshi!", inline=False)
    otherembed.set_footer(text=f"Request by {ctx.author}", icon_url=ctx.author.avatar_url)

    await ctx.send(embed=otherembed)

@bot.command()
@commands.has_role(567737541546082304)
async def clear(ctx, amount: int):
    """Clears the amount of messages that you filled in."""
    await ctx.channel.purge(limit=amount + 1)

async def chng_pr():
    await bot.wait_until_ready()
    await bot.change_presence(activity=discord.Activity(name="enderelijas", type=3), status='idle')
    await bot.change_presence(activity=discord.Activity(name="?help", type=0), status='idle')  

bot.loop.create_task(chng_pr())

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        embed = discord.Embed(title="Error:",
                              description=f"The command `{ctx.invoked_with}` was not found! We suggest you do `?help` to see all of the commands",
                              colour=0xe73c24)
        await ctx.send(embed=embed)
    elif isinstance(error, commands.MissingRole):
        roleid = error.missing_role
        embed = discord.Embed(title="Error:",
                              description=f"You don't have permission to execute `{ctx.invoked_with}`, this requires the `{roleid}` role to be executed",
                              colour=0xe73c24)
        await ctx.send(embed=embed)
    else:
        embed = discord.Embed(title="Error:",
                              description=f"`{error}`",
                              colour=0xe73c24)
        await ctx.send(embed=embed)
        raise error

@bot.event
async def creeper(ctx):
    if "creeper" in message.content:
        await message.channel.send('aww man!')
        
@bot.command()
async def add(ctx, a: int, b: int):
    """Adds 2 numbers together."""
    await ctx.send(a+b)
    
@bot.command()
async def multiply(ctx, a: int, b: int):
    """Multiplies 2 numbers."""
    await ctx.send(a*b)
        
bot.run(os.getenv('TOKEN'))
