import discord
import time
from discord.ext import commands
from discord.types import embed


class Owner(commands.Cog):
    """A cog for global error handling."""
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Owner loaded!")
        # make this print in a different channel

    @commands.command()
    @commands.has_role('Owner')
    async def setstatus(self, ctx: commands.Context, *, text: str):
        """Set the bot's status."""
        await self.bot.change_presence(activity=discord.Game(name=text))

    @commands.command()
    @commands.has_role('Owner')
    async def unload(self, ctx, cog_name):
        """unload cog_name"""
        self.bot.unload_extension(f"cogs.{cog_name}")
        await ctx.send(f"Successfully unloaded {cog_name}")

    @commands.command()
    @commands.has_role('Owner')
    async def load(self, ctx, cog_name):
        """load cog_name"""
        self.bot.load_extension(f"cogs.{cog_name}")
        await ctx.send(f"Successfully loaded {cog_name}")

    @commands.command()
    @commands.has_any_role('Owner')
    async def reload(self, ctx, cog_name):
        """reload cog_name"""
        self.bot.reload_extension(f"cogs.{cog_name}")
        await ctx.send(f"Successfully reloaded {cog_name}.")

    @commands.command(name="ping")
    async def ping(self, ctx: commands.Context):
        """Get the bot's current websocket and API latency."""
        start_time = time.time()
        message = await ctx.send("Testing Ping...")
        end_time = time.time()

        await message.edit(
            content=f"Ping: {round(self.bot.latency * 1000)}ms\nAPI: {round((end_time - start_time) * 1000)}ms")


def setup(bot):
    bot.add_cog(Owner(bot))
