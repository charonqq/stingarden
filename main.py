import discord
from discord.ext import commands
import os

intents = discord.Intents.default()
intents.typing = False
intents.presences = False

bot = commands.Bot(command_prefix='/', intents=intents)


#remove the default help command so that we can write out own
bot.remove_command('help')

# Load extensions (cogs)
initial_extensions = [
    'cogs.help_cog',         # Assuming help_cog.py is in the cogs folder
    'cogs.music_cog_class',  # Assuming music_cog_class.py is in the cogs folder
]

if __name__ == '__main__':
    for extension in initial_extensions:
        bot.load_extension(extension)

# Load the token from environment variables
bot.run(os.getenv("DISCORD_TOKEN"))


#start the bot with our token
bot.run(os.getenv("MTE0NDk0ODk4NjM0NDY0MDYwMw.GeW7vb.9Zwv5u6Cn6P6JlRaI0bZt0qpj3UkgLdtKqa7rY"))