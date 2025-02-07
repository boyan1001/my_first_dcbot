import discord
import os
import math
import random
import json
import asyncio

from discord.ext import commands
from dotenv import load_dotenv

# load dotenv
load_dotenv()
DCBOT_TOKEN = os.getenv("DCBOT_TOKEN")

# intents是要求機器人的權限
intents = discord.Intents.all()
# command_prefix是前綴符號，可以自由選擇($, #, &...)
bot = commands.Bot(command_prefix = "$", intents = intents)


@bot.event
# 當機器人完成啟動
async def on_ready():
    slash = await bot.tree.sync()
    print(f"目前登入身份 --> {bot.user}")
    
@bot.command()
async def load(ctx, extension):
    bot.load_extension(f"src.{extension}")
    await ctx.send(f"Loaded {extension}")

@bot.command()
async def unload(ctx, extension):
    bot.unload_extension(f"src.{extension}")
    await ctx.send(f"Unloaded {extension}")

@bot.command()
async def reload(ctx, extension):
    bot.unload_extension(f"src.{extension}")
    bot.load_extension(f"src.{extension}")
    await ctx.send(f"Reloaded {extension}")

async def main():
    for filename in os.listdir("./src"):
        if filename == "__init__.py" or not filename.endswith(".py"):
            continue
        await bot.load_extension(f"src.{filename[:-3]}")
    await bot.start(DCBOT_TOKEN)

if __name__ == "__main__":
    asyncio.run(main())

