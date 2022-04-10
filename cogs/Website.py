import discord
import time
from discord.ext import commands


class Website(commands.Cog):
    """A cog for global error handling."""
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Website loaded!")
        # make this print in a different channel


def setup(bot):
    bot.add_cog(Website(bot))
