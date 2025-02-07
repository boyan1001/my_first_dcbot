import discord
from discord.ext import commands

class Event(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(member):
        print(f"{member} join!")

    @commands.Cog.listener()
    async def on_member_remove(member):
        print(f"{member} join!") 

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.content == "Hello":
            await message.channel.send("Hello, world!")

async def setup(bot):
    await bot.add_cog(Event(bot))