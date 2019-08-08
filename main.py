from PIL import Image, ImageDraw
import numpy as np


def change(r, g, b, rgb):
    img = Image.open('rgb.jpg')
    rgba_img = img.convert('RGB')
    array = np.asarray(rgba_img)
    for i, line in enumerate(array):
        if i < 180:
            continue
        for j, num in enumerate(line):
            if 160 < num[0] and abs(int(num[1]) - int(num[2])) < 23 and num[1] < 195 and i > 180:
                rgba_img.putpixel((j, i), (r, g, b, 255))
    draw = ImageDraw.Draw(rgba_img)
    draw.text((40, 40), f"r:{r},g:{g},b:{b}   rgb:{rgb}", fill="#0000ff", direction=None)
    rgba_img.show()


def convert_rgb(rgb):
    r = int('0x{}'.format(rgb[1:3]), 16)
    g = int('0x{}'.format(rgb[3:5]), 16)
    b = int('0x{}'.format(rgb[5:7]), 16)
    return r, g, b


if __name__ == '__main__':
    rgb = input("请输入RGB色号:")
    r, g, b = convert_rgb(rgb)
    change(r, g, b, rgb)
