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
    bot.unload_extension('cogs.test')
    print("--------------------")
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('--------------------')
    return

@bot.event
async def on_message(message):
  if isinstance(message.channel, discord.DMChannel):
    embed = discord.Embed(colour=0xa5a5ed)
    hi = message.content
    member = message.author
    logchannel = bot.get_channel(616003171583787013)
    embed.add_field(name=f'There was DM sent from {member} to the bot!', value=hi)
    await logchannel.send(embed=embed)
  await bot.process_commands(message)

@bot.event
async def on_member_join(member):
    channel = bot.get_channel(572461545066594314)
    await channel.send(f"Welcome to the server, {member.mention}. We now have {len(list(bot.get_all_members()))} members.")

@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(572461545066594314)
    await channel.send(f"{member.mention} has left the server. We now have {len(list(bot.get_all_members()))} members.")
    
bot.remove_command('help')

@bot.command()
async def thonk(ctx):
    embed = discord.Embed(colour=0xD5D5D5)
    embed.set_image(url='https://cdn.discordapp.com/emojis/616954827465031709.png?v=1')
    await ctx.send(embed=embed)

@bot.command()
async def minecraft(ctx):
    embed = discord.Embed(colour=0x00FF00)
    embed.add_field(name="Minecraft", value="A really popular sandbox game made by Notch")
    embed.add_field(name="Wikipeadia", value="https://en.wikipedia.org/wiki/Minecraft")
    embed.set_thumbnail(
        url='https://gamepedia.cursecdn.com/minecraft_gamepedia/4/44/Grass_Block_Revision_6.png')
    await ctx.send(embed=embed)

@bot.command()
async def creeper(ctx):
    await ctx.send('Aww Man!')
    
@bot.command()
async def say(ctx, *, args):
    output = ''
    for word in args:
        output += word
        output += ''
    await ctx.send(output)
    await ctx.message.delete() 

@bot.command()
async def party(ctx):
    embed = discord.Embed(color=0xD5D5D5)
    embed.set_image(url='https://i.redd.it/v16fke5bd32z.gif')
    await ctx.send(embed=embed)
    await ctx.message.delete() 

@bot.command()
async def yoshi(ctx):
    embed = discord.Embed(color=0xD5D5D5)
    embed.set_image(url='https://i.kym-cdn.com/photos/images/original/001/417/391/51f.gif')
    await ctx.send(embed=embed)
    await ctx.send('**__SO PHAT__**')
 
@bot.command()
async def ping(ctx):
    embed = discord.Embed(colour=0x00FF00)
    embed.add_field(name="Ping", value=f'🏓 {round(bot.latency * 1000)}ms')
    embed.set_footer(text=f"Request by {ctx.author}", icon_url=ctx.author.avatar_url)
    await ctx.send(embed=embed)
    
@bot.command()
@commands.has_role(570912164051812352)
async def ban(ctx, member: discord.Member, *, reason='No reason provided.'):
    if member.bot == True:
        await member.ban(reason=reason)
        await ctx.message.delete()
        await ctx.send(f'{member} has been banned.')
    else:
        dm = discord.Embed(title="You have been banned from `Ender Network`!", color=0xAA00FF)
        dm.add_field(name="Moderator:",
                        value=ctx.message.author.display_name)
        dm.add_field(name="Reason:", value=f"{reason}")
        dm.set_thumbnail(url=member.avatar_url)
        await member.send(embed=dm)  # Send DM
        await member.ban(reason=reason)  # Ban
        await ctx.message.delete()  # Delete The Message
        await ctx.send('member has been banned.')

@bot.command()
@commands.has_role(570912164051812352)
async def kick(ctx, member: discord.Member, *, reason='No reason provided.'):
    if member.bot == True:
        await member.kick(reason=reason)
        await ctx.message.delete()
        await ctx.send(f'{member} has been kicked.')
    else:
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
async def links(ctx):
    embed = discord.Embed(
        title="EnderBot", description="links", color=0xa5a5ed)

    embed.add_field(
        name="Support Server", value="[Invite link](https://discord.gg/n8AmFXB)", inline=False)

    embed.add_field(
        name="Website", value="[Link](https://enderelijas.tk)", inline=False)

    embed.set_footer(
        text=f"Request by {ctx.author}", icon_url=ctx.author.avatar_url)

    await ctx.send(embed=embed)

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
    
    await ctx.author.send(embed=embed)

    otherembed = discord.Embed(
        title="Enderbot", description="Other Commands:", color=0x570082)

    otherembed.set_thumbnail(
        url='https://i.redd.it/v16fke5bd32z.gif')
    otherembed.add_field(name="?ping", value="Pings the bot.", inline=False)
    otherembed.add_field(name="?help", value="Gives this message.", inline=False)
    otherembed.add_field(name="?links", value="Gives some links of the bot.", inline=False)
    otherembed.add_field(name="?add", value="Adds 2 numbers.", inline=False)
    otherembed.add_field(name="?multiply", value="Multiply 2 numbers.", inline=False)
    otherembed.add_field(name="?minecraft", value="Gives information about Minecraft", inline=False)
    otherembed.add_field(name="?thonk", value="Thonks.", inline=False)
    otherembed.add_field(name="?creeper", value="Aww Man!", inline=False)
    otherembed.add_field(name="?yoshi", value="Displays a phat yoshi!", inline=False)
    otherembed.add_field(
        name="?party", value="It's party time!", inline=False)
    otherembed.set_footer(text=f"Request by {ctx.author}", icon_url=ctx.author.avatar_url)

    await ctx.message.add_reaction('📧')
    await ctx.send("A message has been sent to your DMs.")
    await ctx.author.send(embed=otherembed)

@bot.command()
@commands.has_role(570912164051812352)
async def clear(ctx, amount: int):
    """Clears the amount of messages that you filled in."""
    await ctx.channel.purge(limit=amount + 1)
    
async def chng_pr():
    await bot.wait_until_ready()

    statuses = ["?help", "with perms", "Minecraft", f"with {len(list(bot.get_all_members()))} users"]
    statuses = cycle(statuses)

    while not bot.is_closed():
        status = next(statuses)

        await bot.change_presence(activity=discord.Game(status), status='dnd')

        await asyncio.sleep(15)

bot.loop.create_task(chng_pr())

@bot.command()
@commands.has_any_role(567739987861307413, 567737541546082304)
#@commands.has_role(567739987861307413)
async def load(ctx, extension):
    bot.load_extension(f'cogs.{extension}')
    await ctx.send('Cog Loaded!')

@bot.command()
@commands.has_any_role(567739987861307413, 567737541546082304)
#@commands.has_role(567739987861307413)
async def unload(ctx, extension):
    bot.unload_extension(f'cogs.{extension}')
    await ctx.send('Cog Unloaded!')

for cog in os.listdir("cogs"):
    if cog.endswith(".py") and not cog.startswith("_"):
        try:
            cog = f"cogs.{cog.replace('.py', '')}"
            bot.load_extension(cog)
        except Exception as e:
            print(f"{cog} cannot be loaded.")
            raise e

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        embed = discord.Embed(title="Error:",
                              description=f"The command `{ctx.invoked_with}` was not found! We suggest you do `help` to see all of the commands",
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
        
@bot.command()
async def add(ctx, a: int, b: int):
    """Adds 2 numbers together."""
    await ctx.send(a+b)
    
@bot.command()
async def multiply(ctx, a: int, b: int):
    """Multiplies 2 numbers."""
    await ctx.send(a*b)

TOKEN = os.environ.get("DISCORD_BOT_SECRET")
bot.run(TOKEN)
