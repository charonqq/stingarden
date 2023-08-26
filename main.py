import discord
from discord.ext import commands
import youtube_dl

intents = discord.Intents.default()
intents.voice_states = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    await bot.process_commands(message)

@bot.command()
async def set(ctx):
    await ctx.send("Bot is now active in this server!")

initial_extensions = ['cogs.music']

if __name__ == '__main__':
    for extension in initial_extensions:
        bot.load_extension(extension)

bot.run('MTE0NDk0ODk4NjM0NDY0MDYwMw.GzlBfv.I3CjTs2XfNJd0h8gtzri7HGTSIcbcCsZlxj--0')
