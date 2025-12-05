import pytesseract
from PIL import Image

img = Image.open("static/IMG_4750.jpg")

text = pytesseract.image_to_string(img, lang="jpn")

print(text)