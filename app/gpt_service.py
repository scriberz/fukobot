import openai
from .config import Config

openai.api_key = Config.OPENAI_API_KEY

def get_gpt_response(prompt):
    response = openai.Completion.create(
        engine="text-davinci-004",
        prompt=prompt,
        max_tokens=150
    )
    return response.choices[0].text.strip()
