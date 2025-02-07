import pathlib
import textwrap
import os

import google.generativeai as genai

from IPython.display import display
from IPython.display import Markdown
from dotenv import load_dotenv

def to_markdown(text):
    text = text.replace('•', '  *')
    return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

load_dotenv()
GOOGLE_API_KEY = os.getenv("GEMINI_TOKEN")

genai.configure(api_key=GOOGLE_API_KEY)

model = genai.GenerativeModel('gemini-2.0-flash')

response = model.generate_content("Please write a short story about a robot that is trying to learn how to love.")

print(response.text)