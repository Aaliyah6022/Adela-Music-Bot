import threading
import time
from main import MusicBot


def discord_bot():
    bot = MusicBot()
    bot.run()


if __name__ == "__main__":
    discord_bot()
