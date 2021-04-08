''' Task Module Description '''
from masonite.scheduler.Task import Task
import discord
from discord.ext import commands


class PriceTest(Task):
    ''' Task description '''

    run_every = '1 minute'

    def handle(self):
        """Logic to handle the job."""
        # https://api.dex.guru/v1/tokens/0x6b51231c43b1604815313801db5e9e614914d6e4-bsc

        # discord_base_url = "https://discord.com/api"

        # client = discord.Client()

        bot = commands.Bot(command_prefix='$')

        bot.command()

        bot.add_command(self.test())

        # client.run("ODI5MDg4ODYyNTYzMjA1MTUw.YGzDLA.XDxfFJLSTjdXDL-cxGdVqNgoMjQ")

    def test(self, ctx, arg):
        ctx.send(arg)
