import pytesseract
from PIL import Image

img = Image.open("static/IMG_4750.jpg")

text = pytesseract.image_to_string(img, lang="jpn")

print(text)


from google import genai

import os
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(api_key= os.environ.get("API_KEY"))

response = client.models.generate_content(
    model="gemini-2.5-flash", contents=f"以下のTesseractで画像から文字にしたものを、綺麗な文章にしてみやすくしてください。{text}"
)

print(response.text)
