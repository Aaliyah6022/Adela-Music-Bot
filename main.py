import os
import discord
from discord.ext import commands


class MusicBot(commands.Bot):
    def __init__(self):
        super().__init__(
            command_prefix=self.prefix,
            case_insensitive=True,
            intents=discord.Intents.all(),
            allowed_mentions=discord.AllowedMentions(
                users=True,  # Whether to ping individual user @mentions
                everyone=False,  # Whether to ping @everyone or @here mentions
                roles=False,  # Whether to ping role @mentions
                replied_user=True,  # Whether to ping on replies to messages

            )
        )

    def setup(self):
        print("Running Setup...")
        super().remove_command("Help")

        for cog in os.listdir("./cogs"):
            if cog.endswith(".py"):
                try:
                    cog = f"cogs.{cog.replace('.py', '')}"
                    self.load_extension(cog)
                    print(f"Loaded extension '{cog}'")
                except Exception as e:
                    # print(f"{cog} can not be loaded:")
                    # raise e
                    print(f"Failed to load extension {cog}\n{e}")

        print("Setup complete.")

    def run(self):
        self.setup()

        # with open("data/token.0", "r", encoding="utf-8") as f:
        #    TOKEN = f.read()
        TOKEN = "xxxxxxxxxxxxxxxx"

        print("Running bot...")
        super().run(TOKEN, reconnect=True)

    async def shutdown(self):
        print("Shutting down...")
        await super().close()

    async def on_connect(self):
        print(f"Connected to discord (latency: {self.latency*1000:,.0f} ms).")

    async def on_disconnect(self):
        print("Bot disconected.")

    async def on_ready(self):
        client_id = (await self.application_info()).id
        await super().change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="Spotify"))
        print("Bot ready.")

    @staticmethod
    async def prefix(bot, msg):
        return commands.when_mentioned_or("?")(bot, msg)

    async def process_commands(self, msg):
        ctx = await self.get_context(msg, cls=commands.Context)

        if ctx.command is not None:
            await self.invoke(ctx)

    async def on_message(self, msg):
        if not msg.author.bot:
            await self.process_commands(msg)
