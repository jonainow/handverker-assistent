# app/ai/ai_svar.py

import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

def spør_ai(prompt):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",  # Billigere og raskere modell
        messages=[
            {"role": "system", "content": "Du er en norsk ekspert på bygg og håndverk. Svar kort, tydelig og praktisk."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=300
    )
    return response.choices[0].message.content.strip()
