import discord
import os

from discord.ext import commands
from dotenv import load_dotenv

# load dotenv
load_dotenv()
DCBOT_TOKEN = os.getenv("DCBOT_TOKEN")

# intents是要求機器人的權限
intents = discord.Intents.all()
# command_prefix是前綴符號，可以自由選擇($, #, &...)
bot = commands.Bot(command_prefix = "%", intents = intents)

@bot.event
# 當機器人完成啟動
async def on_ready():
    print(f"目前登入身份 --> {bot.user}")

@bot.command()
# 輸入%Hello呼叫指令
async def Hello(ctx):
    # 回覆Hello, world!
    await ctx.send("Hello, world!")

bot.run(DCBOT_TOKEN)
