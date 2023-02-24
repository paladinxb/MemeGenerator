from PIL import Image, ImageDraw, ImageFont
import random
import os
image_paths = ('C:/Users/79842/memegenerator/memes')

# List of random words
words = ['lol', 'rofl', 'lmao', 'haha', "BIG L", "BIG W"]

# Select a random image
image_path = random.choice(image_paths)

# Load the image
image = Image.open('meme1.jpg')

# Get the image size
width, height = image.size

# Create a drawing context
draw = ImageDraw.Draw(image)

# Select a random font and font size
font = ImageFont.truetype('arial.ttf', random.randint(40, 100))

# Select a random word
word = random.choice(words)

# Get the size of the text
text_width, text_height = draw.textlength(word, font)

# Calculate the position of the text
x = random.randint(0, width - text_width)
y = random.randint(0, height - text_height)

# Draw the text on the image
draw.text((x, y), word, font=font)

# Save the meme
image.save('meme1.jpg')