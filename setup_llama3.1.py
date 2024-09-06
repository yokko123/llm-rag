from groq import Groq
from dotenv import load_dotenv
import os
load_dotenv()

key = os.getenv('GROQ_API_KEY')

client = Groq(api_key=key)
completion = client.chat.completions.create(
    model="llama-3.1-8b-instant",
    messages=[
        {
            "role": "user",
            "content": "what is chlroophyll?"
        }
    ],
    temperature=1,
    max_tokens=1024,
    top_p=1,
    stream=True,
    stop=None,
)

for chunk in completion:
    print(chunk.choices[0].delta.content or "", end="")
