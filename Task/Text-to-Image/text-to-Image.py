from num2words import num2words
from PIL import Image, ImageDraw, ImageFont

def number_to_image(value, filename="output.png"):
    text = num2words(value).title()

    canvas = Image.new("RGB", (800, 300), "white")
    pen = ImageDraw.Draw(canvas)

    try:
        typeface = ImageFont.truetype("arial.ttf", 60)
    except:
        typeface = ImageFont.load_default()

    left, top, right, bottom = pen.textbbox((0, 0), text, font=typeface)
    text_width = right - left
    text_height = bottom - top

    position_x = (canvas.width - text_width) / 2
    position_y = (canvas.height - text_height) / 2

    pen.text((position_x, position_y), text, fill="black", font=typeface)

    canvas.save(filename)
    print(f"Image saved as {filename}")

user_input = int(input("Enter a number: "))
number_to_image(user_input)
