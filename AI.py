from google import genai

import os
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(api_key= os.environ.get("API_KEY"))

response = client.models.generate_content(
    model="gemini-2.5-flash", contents="好きな食べ物はなんですか"
)

print(response.text)
