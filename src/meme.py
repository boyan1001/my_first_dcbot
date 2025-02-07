import discord
import random
import json
import os

from discord.ext import commands
from discord import app_commands

class Meme(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # @commands.command()
    # async def meme(self, ctx):
    #     # find path
    #     curr = os.getcwd()
    #     path = curr + "\\docs\\meme"
    #     print(path)

    #     file = open(path + "\\meme.json", "r", encoding="utf-8")
    #     mjson = json.load(file)
    #     mlist = mjson["map"]

    #     n = random.randint(0, 13)
    #     filename = mlist[n]['name']
    #     path = path + "\\" + filename
        
    #     pic = discord.File(path)
    #     file.close()
    #     await ctx.send(file = pic)
    
    @app_commands.command(name = "meme", description = "輸出一張迷因圖片")
    async def meme(self, interaction: discord.Interaction):
        # find path
        curr = os.getcwd()
        path = curr + "\\docs\\meme"
        print(path)

        file = open(path + "\\meme.json", "r", encoding="utf-8")
        mjson = json.load(file)
        mlist = mjson["map"]

        n = random.randint(0, 13)
        filename = mlist[n]['name']
        path = path + "\\" + filename
        
        pic = discord.File(path)
        file.close()
        await interaction.response.send_message(file = pic)

async def setup(bot):
    await bot.add_cog(Meme(bot))