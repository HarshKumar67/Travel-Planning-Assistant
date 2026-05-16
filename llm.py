from groq import Groq
from dotenv import load_dotenv
import os
import re

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

def clean_text(text):

    # Remove markdown bold
    text = text.replace("**", "")

    # Remove markdown headers
    text = text.replace("###", "")
    text = text.replace("##", "")
    text = text.replace("#", "")

    # Remove extra stars
    text = text.replace("*", "•")

    # Remove long separators
    text = re.sub(r"=+", "", text)

    # Remove excessive dashes
    text = re.sub(r"-{3,}", "", text)

    return text.strip()

def generate_response(prompt):

    response = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        model="llama-3.1-8b-instant",
    )

    return response.choices[0].message.content