# ai_generator.py

import openai
from config import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY

def generate_post():
    prompt = "Write a short, engaging AI-related social media post for Telegram."

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # Make sure your key supports this
        messages=[
            {"role": "system", "content": "You are a helpful assistant that writes AI social media posts."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=100,
        temperature=0.8,
    )

    return response['choices'][0]['message']['content'].strip()
