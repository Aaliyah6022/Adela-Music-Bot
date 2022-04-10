import discord
from enum import Enum
from discord.ext import commands


class ErrorHandler(commands.Cog):
    """A cog for global error handling."""
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("ErrorHandler loaded!")
        # make this print in a different channel

    class ErrorTypes(Enum):
        commands.CommandNotFound = 0
        commands.CommandOnCooldown = 1
        commands.MissingPermissions = 2
        commands.CommandNotFound = 3
        commands.UserInputError = 4
        commands.MissingRequiredArgument = 5
        commands.ArgumentParsingError = 6
        commands.UnexpectedQuoteError = 7
        commands.InvalidEndOfQuotedStringError = 8
        commands.ExpectedClosingQuoteError = 9
        commands.BadArgument = 10
        commands.BadUnionArgument = 11
        commands.PrivateMessageOnly = 12
        commands.NoPrivateMessage = 13
        commands.CheckFailure = 14
        commands.CheckAnyFailure = 15
        commands.CommandNotFound = 16
        commands.DisabledCommand = 17
        commands.CommandInvokeError = 18
        commands.TooManyArguments = 19
        commands.UserInputError = 20
        commands.CommandOnCooldown = 21
        commands.MaxConcurrencyReached = 22
        commands.NotOwner = 23
        commands.MessageNotFound = 24
        commands.MemberNotFound = 25
        commands.GuildNotFound = 26
        commands.UserNotFound = 27
        commands.ChannelNotFound = 28
        commands.ChannelNotReadable = 29
        commands.BadColourArgument = 30
        commands.RoleNotFound = 31
        commands.BadInviteArgument = 32
        commands.EmojiNotFound = 33
        commands.PartialEmojiConversionFailure = 34
        commands.BadBoolArgument = 35
        commands.MissingPermissions = 36
        commands.BotMissingPermissions = 37
        commands.MissingRole = 38
        commands.BotMissingRole = 39
        commands.MissingAnyRole = 40
        commands.BotMissingAnyRole = 41
        commands.NSFWChannelRequired = 42
        commands.ExtensionError = 43
        commands.ExtensionAlreadyLoaded = 44
        commands.ExtensionNotLoaded = 45
        commands.NoEntryPointError = 46
        commands.ExtensionFailed = 47
        commands.ExtensionNotFound = 48

    @commands.Cog.listener()
    async def on_command_error(self, ctx: commands.Context, error: ErrorTypes):
        """A global error handler cog."""
        match error:
            case 0:
                embed = discord.Embed(title="⚠️ **Something went wrong** ⚠️",
                                      color=0x2e46ff)
                embed.set_author(name=f"{ctx.author.name}",
                                 icon_url=f"{ctx.author.avatar}")
                embed.add_field(name="Error Type: ", value=f"{error}", inline=True)
                embed.set_footer(text="Made with ❤️ by LunaLynx")
            case 1:
                embed = discord.Embed(title="⚠️ **Something went wrong** ⚠️",
                                      color=0x2e46ff)
                embed.set_author(name=f"{ctx.author.name}",
                                 icon_url=f"{ctx.author.avatar}")
                embed.add_field(name="Error Type: ", value=f"{error}", inline=True)
                embed.set_footer(text="Made with ❤️ by LunaLynx")
            case 2:
                embed = discord.Embed(title="⚠️ **Something went wrong** ⚠️",
                                      color=0x2e46ff)
                embed.set_author(name=f"{ctx.author.name}",
                                 icon_url=f"{ctx.author.avatar}")
                embed.add_field(name="Error Type: ", value=f"{error}", inline=True)
                embed.set_footer(text="Made with ❤️ by LunaLynx")
            case 3:
                embed = discord.Embed(title="⚠️ **Something went wrong** ⚠️",
                                      color=0x2e46ff)
                embed.set_author(name=f"{ctx.author.name}",
                                 icon_url=f"{ctx.author.avatar}")
                embed.add_field(name="Error Type: ", value=f"{error}", inline=True)
                embed.set_footer(text="Made with ❤️ by LunaLynx")
            case 4:
                embed = discord.Embed(title="⚠️ **Something went wrong** ⚠️",
                                      color=0x2e46ff)
                embed.set_author(name=f"{ctx.author.name}",
                                 icon_url=f"{ctx.author.avatar}")
                embed.add_field(name="Error Type: ", value=f"{error}", inline=True)
                embed.set_footer(text="Made with ❤️ by LunaLynx")
            case 5:
                embed = discord.Embed(title="⚠️ **Something went wrong** ⚠️",
                                      color=0x2e46ff)
                embed.set_author(name=f"{ctx.author.name}",
                                 icon_url=f"{ctx.author.avatar}")
                embed.add_field(name="Error Type: ", value=f"{error}", inline=True)
                embed.set_footer(text="Made with ❤️ by LunaLynx")
            case 6:
                embed = discord.Embed(title="⚠️ **Something went wrong** ⚠️",
                                      color=0x2e46ff)
                embed.set_author(name=f"{ctx.author.name}",
                                 icon_url=f"{ctx.author.avatar}")
                embed.add_field(name="Error Type: ", value=f"{error}", inline=True)
                embed.set_footer(text="Made with ❤️ by LunaLynx")
            case 7:
                embed = discord.Embed(title="⚠️ **Something went wrong** ⚠️",
                                      color=0x2e46ff)
                embed.set_author(name=f"{ctx.author.name}",
                                 icon_url=f"{ctx.author.avatar}")
                embed.add_field(name="Error Type: ", value=f"{error}", inline=True)
                embed.set_footer(text="Made with ❤️ by LunaLynx")
            case 8:
                embed = discord.Embed(title="⚠️ **Something went wrong** ⚠️",
                                      color=0x2e46ff)
                embed.set_author(name=f"{ctx.author.name}",
                                 icon_url=f"{ctx.author.avatar}")
                embed.add_field(name="Error Type: ", value=f"{error}", inline=True)
                embed.set_footer(text="Made with ❤️ by LunaLynx")
            case 9:
                embed = discord.Embed(title="⚠️ **Something went wrong** ⚠️",
                                      color=0x2e46ff)
                embed.set_author(name=f"{ctx.author.name}",
                                 icon_url=f"{ctx.author.avatar}")
                embed.add_field(name="Error Type: ", value=f"{error}", inline=True)
                embed.set_footer(text="Made with ❤️ by LunaLynx")
            case 10:
                embed = discord.Embed(title="⚠️ **Something went wrong** ⚠️",
                                      color=0x2e46ff)
                embed.set_author(name=f"{ctx.author.name}",
                                 icon_url=f"{ctx.author.avatar}")
                embed.add_field(name="Error Type: ", value=f"{error}", inline=True)
                embed.set_footer(text="Made with ❤️ by LunaLynx")
            case 11:
                embed = discord.Embed(title="⚠️ **Something went wrong** ⚠️",
                                      color=0x2e46ff)
                embed.set_author(name=f"{ctx.author.name}",
                                 icon_url=f"{ctx.author.avatar}")
                embed.add_field(name="Error Type: ", value=f"{error}", inline=True)
                embed.set_footer(text="Made with ❤️ by LunaLynx")
            case 12:
                embed = discord.Embed(title="⚠️ **Something went wrong** ⚠️",
                                      color=0x2e46ff)
                embed.set_author(name=f"{ctx.author.name}",
                                 icon_url=f"{ctx.author.avatar}")
                embed.add_field(name="Error Type: ", value=f"{error}", inline=True)
                embed.set_footer(text="Made with ❤️ by LunaLynx")
            case 13:
                embed = discord.Embed(title="⚠️ **Something went wrong** ⚠️",
                                      color=0x2e46ff)
                embed.set_author(name=f"{ctx.author.name}",
                                 icon_url=f"{ctx.author.avatar}")
                embed.add_field(name="Error Type: ", value=f"{error}", inline=True)
                embed.set_footer(text="Made with ❤️ by LunaLynx")
            case 14:
                embed = discord.Embed(title="⚠️ **Something went wrong** ⚠️",
                                      color=0x2e46ff)
                embed.set_author(name=f"{ctx.author.name}",
                                 icon_url=f"{ctx.author.avatar}")
                embed.add_field(name="Error Type: ", value=f"{error}", inline=True)
                embed.set_footer(text="Made with ❤️ by LunaLynx")
            case 15:
                embed = discord.Embed(title="⚠️ **Something went wrong** ⚠️",
                                      color=0x2e46ff)
                embed.set_author(name=f"{ctx.author.name}",
                                 icon_url=f"{ctx.author.avatar}")
                embed.add_field(name="Error Type: ", value=f"{error}", inline=True)
                embed.set_footer(text="Made with ❤️ by LunaLynx")
            case 16:
                embed = discord.Embed(title="⚠️ **Something went wrong** ⚠️",
                                      color=0x2e46ff)
                embed.set_author(name=f"{ctx.author.name}",
                                 icon_url=f"{ctx.author.avatar}")
                embed.add_field(name="Error Type: ", value=f"{error}", inline=True)
                embed.set_footer(text="Made with ❤️ by LunaLynx")
            case 17:
                embed = discord.Embed(title="⚠️ **Something went wrong** ⚠️",
                                      color=0x2e46ff)
                embed.set_author(name=f"{ctx.author.name}",
                                 icon_url=f"{ctx.author.avatar}")
                embed.add_field(name="Error Type: ", value=f"{error}", inline=True)
                embed.set_footer(text="Made with ❤️ by LunaLynx")
            case 18:
                embed = discord.Embed(title="⚠️ **Something went wrong** ⚠️",
                                      color=0x2e46ff)
                embed.set_author(name=f"{ctx.author.name}",
                                 icon_url=f"{ctx.author.avatar}")
                embed.add_field(name="Error Type: ", value=f"{error}", inline=True)
                embed.set_footer(text="Made with ❤️ by LunaLynx")
            case 19:
                embed = discord.Embed(title="⚠️ **Something went wrong** ⚠️",
                                      color=0x2e46ff)
                embed.set_author(name=f"{ctx.author.name}",
                                 icon_url=f"{ctx.author.avatar}")
                embed.add_field(name="Error Type: ", value=f"{error}", inline=True)
                embed.set_footer(text="Made with ❤️ by LunaLynx")
            case 20:
                embed = discord.Embed(title="⚠️ **Something went wrong** ⚠️",
                                      color=0x2e46ff)
                embed.set_author(name=f"{ctx.author.name}",
                                 icon_url=f"{ctx.author.avatar}")
                embed.add_field(name="Error Type: ", value=f"{error}", inline=True)
                embed.set_footer(text="Made with ❤️ by LunaLynx")
            case 21:
                embed = discord.Embed(title="⚠️ **Something went wrong** ⚠️",
                                      color=0x2e46ff)
                embed.set_author(name=f"{ctx.author.name}",
                                 icon_url=f"{ctx.author.avatar}")
                embed.add_field(name="Error Type: ", value=f"{error}", inline=True)
                embed.set_footer(text="Made with ❤️ by LunaLynx")
            case 22:
                embed = discord.Embed(title="⚠️ **Something went wrong** ⚠️",
                                      color=0x2e46ff)
                embed.set_author(name=f"{ctx.author.name}",
                                 icon_url=f"{ctx.author.avatar}")
                embed.add_field(name="Error Type: ", value=f"{error}", inline=True)
                embed.set_footer(text="Made with ❤️ by LunaLynx")
            case 23:
                embed = discord.Embed(title="⚠️ **Something went wrong** ⚠️",
                                      color=0x2e46ff)
                embed.set_author(name=f"{ctx.author.name}",
                                 icon_url=f"{ctx.author.avatar}")
                embed.add_field(name="Error Type: ", value=f"{error}", inline=True)
                embed.set_footer(text="Made with ❤️ by LunaLynx")
            case 24:
                embed = discord.Embed(title="⚠️ **Something went wrong** ⚠️",
                                      color=0x2e46ff)
                embed.set_author(name=f"{ctx.author.name}",
                                 icon_url=f"{ctx.author.avatar}")
                embed.add_field(name="Error Type: ", value=f"{error}", inline=True)
                embed.set_footer(text="Made with ❤️ by LunaLynx")
            case 25:
                embed = discord.Embed(title="⚠️ **Something went wrong** ⚠️",
                                      color=0x2e46ff)
                embed.set_author(name=f"{ctx.author.name}",
                                 icon_url=f"{ctx.author.avatar}")
                embed.add_field(name="Error Type: ", value=f"{error}", inline=True)
                embed.set_footer(text="Made with ❤️ by LunaLynx")
            case 26:
                embed = discord.Embed(title="⚠️ **Something went wrong** ⚠️",
                                      color=0x2e46ff)
                embed.set_author(name=f"{ctx.author.name}",
                                 icon_url=f"{ctx.author.avatar}")
                embed.add_field(name="Error Type: ", value=f"{error}", inline=True)
                embed.set_footer(text="Made with ❤️ by LunaLynx")
            case 27:
                embed = discord.Embed(title="⚠️ **Something went wrong** ⚠️",
                                      color=0x2e46ff)
                embed.set_author(name=f"{ctx.author.name}",
                                 icon_url=f"{ctx.author.avatar}")
                embed.add_field(name="Error Type: ", value=f"{error}", inline=True)
                embed.set_footer(text="Made with ❤️ by LunaLynx")
            case 28:
                embed = discord.Embed(title="⚠️ **Something went wrong** ⚠️",
                                      color=0x2e46ff)
                embed.set_author(name=f"{ctx.author.name}",
                                 icon_url=f"{ctx.author.avatar}")
                embed.add_field(name="Error Type: ", value=f"{error}", inline=True)
                embed.set_footer(text="Made with ❤️ by LunaLynx")
            case 29:
                embed = discord.Embed(title="⚠️ **Something went wrong** ⚠️",
                                      color=0x2e46ff)
                embed.set_author(name=f"{ctx.author.name}",
                                 icon_url=f"{ctx.author.avatar}")
                embed.add_field(name="Error Type: ", value=f"{error}", inline=True)
                embed.set_footer(text="Made with ❤️ by LunaLynx")
            case 30:
                embed = discord.Embed(title="⚠️ **Something went wrong** ⚠️",
                                      color=0x2e46ff)
                embed.set_author(name=f"{ctx.author.name}",
                                 icon_url=f"{ctx.author.avatar}")
                embed.add_field(name="Error Type: ", value=f"{error}", inline=True)
                embed.set_footer(text="Made with ❤️ by LunaLynx")
            case 31:
                embed = discord.Embed(title="⚠️ **Something went wrong** ⚠️",
                                      color=0x2e46ff)
                embed.set_author(name=f"{ctx.author.name}",
                                 icon_url=f"{ctx.author.avatar}")
                embed.add_field(name="Error Type: ", value=f"{error}", inline=True)
                embed.set_footer(text="Made with ❤️ by LunaLynx")
            case 32:
                embed = discord.Embed(title="⚠️ **Something went wrong** ⚠️",
                                      color=0x2e46ff)
                embed.set_author(name=f"{ctx.author.name}",
                                 icon_url=f"{ctx.author.avatar}")
                embed.add_field(name="Error Type: ", value=f"{error}", inline=True)
                embed.set_footer(text="Made with ❤️ by LunaLynx")
            case 33:
                embed = discord.Embed(title="⚠️ **Something went wrong** ⚠️",
                                      color=0x2e46ff)
                embed.set_author(name=f"{ctx.author.name}",
                                 icon_url=f"{ctx.author.avatar}")
                embed.add_field(name="Error Type: ", value=f"{error}", inline=True)
                embed.set_footer(text="Made with ❤️ by LunaLynx")
            case 34:
                embed = discord.Embed(title="⚠️ **Something went wrong** ⚠️",
                                      color=0x2e46ff)
                embed.set_author(name=f"{ctx.author.name}",
                                 icon_url=f"{ctx.author.avatar}")
                embed.add_field(name="Error Type: ", value=f"{error}", inline=True)
                embed.set_footer(text="Made with ❤️ by LunaLynx")
            case 35:
                embed = discord.Embed(title="⚠️ **Something went wrong** ⚠️",
                                      color=0x2e46ff)
                embed.set_author(name=f"{ctx.author.name}",
                                 icon_url=f"{ctx.author.avatar}")
                embed.add_field(name="Error Type: ", value=f"{error}", inline=True)
                embed.set_footer(text="Made with ❤️ by LunaLynx")
            case 36:
                embed = discord.Embed(title="⚠️ **Something went wrong** ⚠️",
                                      color=0x2e46ff)
                embed.set_author(name=f"{ctx.author.name}",
                                 icon_url=f"{ctx.author.avatar}")
                embed.add_field(name="Error Type: ", value=f"{error}", inline=True)
                embed.set_footer(text="Made with ❤️ by LunaLynx")
            case 37:
                embed = discord.Embed(title="⚠️ **Something went wrong** ⚠️",
                                      color=0x2e46ff)
                embed.set_author(name=f"{ctx.author.name}",
                                 icon_url=f"{ctx.author.avatar}")
                embed.add_field(name="Error Type: ", value=f"{error}", inline=True)
                embed.set_footer(text="Made with ❤️ by LunaLynx")
            case 38:
                embed = discord.Embed(title="⚠️ **Something went wrong** ⚠️",
                                      color=0x2e46ff)
                embed.set_author(name=f"{ctx.author.name}",
                                 icon_url=f"{ctx.author.avatar}")
                embed.add_field(name="Error Type: ", value=f"{error}", inline=True)
                embed.set_footer(text="Made with ❤️ by LunaLynx")
            case 39:
                embed = discord.Embed(title="⚠️ **Something went wrong** ⚠️",
                                      color=0x2e46ff)
                embed.set_author(name=f"{ctx.author.name}",
                                 icon_url=f"{ctx.author.avatar}")
                embed.add_field(name="Error Type: ", value=f"{error}", inline=True)
                embed.set_footer(text="Made with ❤️ by LunaLynx")
            case 40:
                embed = discord.Embed(title="⚠️ **Something went wrong** ⚠️",
                                      color=0x2e46ff)
                embed.set_author(name=f"{ctx.author.name}",
                                 icon_url=f"{ctx.author.avatar}")
                embed.add_field(name="Error Type: ", value=f"{error}", inline=True)
                embed.set_footer(text="Made with ❤️ by LunaLynx")
            case 41:
                embed = discord.Embed(title="⚠️ **Something went wrong** ⚠️",
                                      color=0x2e46ff)
                embed.set_author(name=f"{ctx.author.name}",
                                 icon_url=f"{ctx.author.avatar}")
                embed.add_field(name="Error Type: ", value=f"{error}", inline=True)
                embed.set_footer(text="Made with ❤️ by LunaLynx")
            case 42:
                embed = discord.Embed(title="⚠️ **Something went wrong** ⚠️",
                                      color=0x2e46ff)
                embed.set_author(name=f"{ctx.author.name}",
                                 icon_url=f"{ctx.author.avatar}")
                embed.add_field(name="Error Type: ", value=f"{error}", inline=True)
                embed.set_footer(text="Made with ❤️ by LunaLynx")
            case 43:
                embed = discord.Embed(title="⚠️ **Something went wrong** ⚠️",
                                      color=0x2e46ff)
                embed.set_author(name=f"{ctx.author.name}",
                                 icon_url=f"{ctx.author.avatar}")
                embed.add_field(name="Error Type: ", value=f"{error}", inline=True)
                embed.set_footer(text="Made with ❤️ by LunaLynx")
            case 44:
                embed = discord.Embed(title="⚠️ **Something went wrong** ⚠️",
                                      color=0x2e46ff)
                embed.set_author(name=f"{ctx.author.name}",
                                 icon_url=f"{ctx.author.avatar}")
                embed.add_field(name="Error Type: ", value=f"{error}", inline=True)
                embed.set_footer(text="Made with ❤️ by LunaLynx")
            case 45:
                embed = discord.Embed(title="⚠️ **Something went wrong** ⚠️",
                                      color=0x2e46ff)
                embed.set_author(name=f"{ctx.author.name}",
                                 icon_url=f"{ctx.author.avatar}")
                embed.add_field(name="Error Type: ", value=f"{error}", inline=True)
                embed.set_footer(text="Made with ❤️ by LunaLynx")
            case 46:
                embed = discord.Embed(title="⚠️ **Something went wrong** ⚠️",
                                      color=0x2e46ff)
                embed.set_author(name=f"{ctx.author.name}",
                                 icon_url=f"{ctx.author.avatar}")
                embed.add_field(name="Error Type: ", value=f"{error}", inline=True)
                embed.set_footer(text="Made with ❤️ by LunaLynx")
            case 47:
                embed = discord.Embed(title="⚠️ **Something went wrong** ⚠️",
                                      color=0x2e46ff)
                embed.set_author(name=f"{ctx.author.name}",
                                 icon_url=f"{ctx.author.avatar}")
                embed.add_field(name="Error Type: ", value=f"{error}", inline=True)
                embed.set_footer(text="Made with ❤️ by LunaLynx")
            case 48:
                embed = discord.Embed(title="⚠️ **Something went wrong** ⚠️",
                                      color=0x2e46ff)
                embed.set_author(name=f"{ctx.author.name}",
                                 icon_url=f"{ctx.author.avatar}")
                embed.add_field(name="Error Type: ", value=f"{error}", inline=True)
                embed.set_footer(text="Made with ❤️ by LunaLynx")
            case _:
                embed = discord.Embed(title="⚠️ **Something went wrong** ⚠️",
                                      color=0x2e46ff)
                embed.set_author(name=f"{ctx.author.name}",
                                 icon_url=f"{ctx.author.avatar}")
                embed.add_field(name="Error Type: ", value=f"{error}", inline=True)
                embed.set_footer(text="Made with ❤️ by LunaLynx")

        await ctx.send(embed=embed, delete_after=10)
        await ctx.message.delete(delay=10)


def setup(bot):
    bot.add_cog(ErrorHandler(bot))
