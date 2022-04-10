import discord
import sys
import platform
from discord.ext import commands, pages


class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.pages = [
            discord.Embed(title="About Adela", url="https://www.youtube.com/watch?v=h8Bb_wJvvVs&list=RDMM&index=11", description="Click the link above to see check the official website", color=0x1692d0),
            discord.Embed(title="Music", color=0xdf4b0c),
            discord.Embed(title="Work in progress...", color=0xdf4b0c),
            discord.Embed(title="Online Documentation", url="https://www.youtube.com/watch?v=h8Bb_wJvvVs&list=RDMM&index=11", description="Click the link above to see check the online manual", color=0x45f514)
        ]

        # page 1 aka About
        self.pages[0].add_field(name="Created by: ", value="LunaLynx#7219", inline=True)
        self.pages[0].add_field(name="Python Version: ", value=platform.python_version(), inline=True)
        self.pages[0].add_field(name="Framework: ", value="[Pycord %s :two_hearts:](https://docs.pycord.dev/en/master/)" % discord.__version__, inline=True)
        # page 2 aka Music
        self.pages[1].add_field(name="join", value="Joins the vc with you", inline=True)
        self.pages[1].add_field(name="play", value="link | song name", inline=True)
        self.pages[1].add_field(name="pause", value="Pauses the music", inline=True)
        self.pages[1].add_field(name="resume", value="Resumes the music", inline=True)
        self.pages[1].add_field(name="queue", value="Shows the queue", inline=True)
        self.pages[1].add_field(name="stop", value="Kicks the bot", inline=True)
        self.pages[1].set_footer(text="Made with ❤️ by LunaLynx")

    def get_pages(self):
        return self.pages

    @commands.command()
    async def help(self, ctx: commands.Context):
        """Demonstrates using the paginator with a prefix-based command."""
        paginator = pages.Paginator(pages=self.get_pages(), use_default_buttons=False)
        # paginator.add_button(pages.PaginatorButton("first", label="<<-", style=discord.ButtonStyle.green))
        paginator.add_button(pages.PaginatorButton("prev", label="<-", style=discord.ButtonStyle.green))
        paginator.add_button(pages.PaginatorButton("page_indicator", style=discord.ButtonStyle.gray, disabled=True))
        paginator.add_button(pages.PaginatorButton("next", label="->", style=discord.ButtonStyle.green))
        # paginator.add_button(pages.PaginatorButton("last", label="->>", style=discord.ButtonStyle.green))
        await paginator.send(ctx)


def setup(bot):
    bot.add_cog(Help(bot))
