import os
import random
from random import randint
from PIL import Image, ImageDraw, ImageFont

font = ImageFont.truetype('arial.ttf', random.randint(40, 100))

image_dir = ('C:/Users/79842/memegenerator/memes')
image_files = os.listdir(image_dir)

words = ["BIG W", "BIG L", "LOL", "ROFL", "WTF", "If u know u know", "Let it be", "OMG", "ASAP BABE"]

def create_meme():
    image_file = random.choice(image_files)
    image = Image.open(os.path.join(image_dir, image_file))
    height = image.height
    width = image.width
    draw = ImageDraw.Draw(image)
    sentence = random.choice(words)
    x = randint(300, 350)
    y = randint(300, 350)
    draw.text((x, y), sentence, fill=1280128, font=font)
    return image

while True: 
    # запрос на продолжение работы
    answer = input("Введите 'Продолжить' для создания файла или 'Остановить' для выхода: ")
    
    # если пользователь вводит 'Остановить', завершаем цикл
    if answer == "Остановить":
        break
    elif answer == "Продолжить":
        meme_name = input("Введите имя файла: ")
        file_extension = ".png"
        png_filename = f"{meme_name}{file_extension}"
        meme_image = create_meme()
        meme_image.save(png_filename)
        #meme_image.show()
    else:
        print("Неверный ввод. Пожалуйста, введите 'Продолжить' или 'Остановить'.")
