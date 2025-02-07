import discord
import random
import pathlib
import textwrap
import os

import google.generativeai as genai

from discord.ext import commands
from discord import app_commands

from IPython.display import display
from IPython.display import Markdown
from dotenv import load_dotenv

class Gemini(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

        load_dotenv()
        GOOGLE_API_KEY = os.getenv("GEMINI_TOKEN")
        genai.configure(api_key=GOOGLE_API_KEY)
        self.model = genai.GenerativeModel('gemini-2.0-flash')
    
    @app_commands.command(name="chat", description="與Gemini聊天")
    @app_commands.describe(line="輸入文字與Gemini聊天")
    async def chat(self, interaction: discord.Interaction, line: str):
        await interaction.response.defer()  # 延遲回覆

        try:
            response = self.model.generate_content(line)
            text = response.text

            if not text:
                await interaction.followup.send("我不知道該怎麼回答您的問題")
                return

            await interaction.followup.send(text)

        except Exception as e:
            await interaction.followup.send(f"發生錯誤：{e}")

async def setup(bot):
    await bot.add_cog(Gemini(bot))