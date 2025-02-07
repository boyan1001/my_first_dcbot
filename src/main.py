import discord
from discord.ext import commands

class Main(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    # 輸入%Hello呼叫指令
    async def Hello(self, ctx):
        # 回覆Hello, world!
        await ctx.send("Hello, world!")

    @commands.command()
    # check the latency of the bot
    async def ping(self, ctx):
        await ctx.send(f"Pong! {round(self.bot.latency * 1000)}ms")

async def setup(bot):
    await bot.add_cog(Main(bot))