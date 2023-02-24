import os
import random
from random import randint
from PIL import Image, ImageDraw, ImageFont

font = ImageFont.truetype('arial.ttf', random.randint(40, 100))

image_dir = ('C:/Users/79842/memegenerator/memes')

image_files = os.listdir(image_dir)

image_file = random.choice(image_files)

image = Image.open(os.path.join(image_dir, image_file))

width, height = image.size

draw = ImageDraw.Draw(image)

words = ["BIG W", "BIG L", "LOL", "ROFL"]

sentence = random.choice(words)


#text_width, text_height = draw.textlength(words, font)
#x = (width - text_width) / 2
#y = height - text_height - 50
x = randint(200, 600)
y = randint(200, 700)

draw.text((x, y), sentence, fill=1280128, font=font)

image.save('meme.png')
