import discord
from discord.ext import tasks, commands


class MyCog(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.index = 0
        self.printer.start()

    def cog_unload(self):
        self.printer.cancel()

    @tasks.loop(seconds=60.0)
    async def something(self):
        print(self.index)
        self.index += 1
        if self.index == 10:
            channel = self.bot.get_channel(613426733424836653)
            general = self.bot.get_channel(613426184025407549)
            await channel.send('Remember to spam here not in {general}')
            self.index = 0

    @something.before_loop
    async def before_something(self):
        print('waiting...')
        await self.bot.wait_until_ready()


def setup(bot):
    bot.add_cog(MyCog(bot))
