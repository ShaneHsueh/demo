"""
File: mirror_lake.py
----------------------------------
This file reads in mt-rainier.jpg and
makes a new image that creates a mirror
lake vibe by placing an inverse image of
mt-rainier.jpg below the original one.
"""
from simpleimage import SimpleImage


def reflect(filename):
    """
    Creates a mirror lake vibe.
    """
    img = SimpleImage(filename)
    new_img = SimpleImage.blank(img.width, img.height * 2)
    for x in range(img.width):
        for y in range(img.height):
            pixel = img.get_pixel(x, y)  # 有顏色的

            new_pixel1 = new_img.get_pixel(x, y)                   # 上圖
            new_pixel2 = new_img.get_pixel(x, new_img.height-y-1)  # 下圖

            # 填滿上圖
            new_pixel1.red = pixel.red
            new_pixel1.green = pixel.green
            new_pixel1.blue = pixel.blue

            # 填滿下圖
            new_pixel2.red = pixel.red
            new_pixel2.green = pixel.green
            new_pixel2.blue = pixel.blue
    return new_img


def main():
    """
    This file creates a mirror lake vibe.
    """
    original_mt = SimpleImage('images/mt-rainier.jpg')
    original_mt.show()
    reflected = reflect('images/mt-rainier.jpg')
    reflected.show()


if __name__ == '__main__':
    main()
