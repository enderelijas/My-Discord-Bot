import discord
from discord.ext import tasks, commands


class MyCog(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.index = 0
        self.printer.start()

    def cog_unload(self):
        self.printer.cancel()

    @tasks.loop(seconds=1.0)
    async def printer(self):
        print(self.index)
        self.index += 1
        if self.index == 10:
            channel = self.bot.get_channel(607205666754658324)
            await channel.send('test')
            self.index = 0

    @printer.before_loop
    async def before_printer(self):
        print('waiting...')
        await self.bot.wait_until_ready()


def setup(bot):
    bot.add_cog(MyCog(bot))
