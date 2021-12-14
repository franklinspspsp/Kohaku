import discord
from discord.ext import commands
from new.config import settings

bot = commands.Bot(command_prefix=settings['prefix'])

async def hello(ctx):
    author = ctx.message.author
    await ctx.send(f'Hello {author.mention}!')

bot.run(settings['token'])