"""
File: best_photoshop_award.py
----------------------------------
This file creates a photoshopped image
that is going to compete for the Best
Photoshop Award for SC001.
Please put all the images you will use in the image_contest folder
and make sure to choose the right folder when loading your images.
"""
from simpleimage import SimpleImage


# Controls the threshold of detecting gray pixel
GRAY_PIXEL = 9
# Controls the upper bound for black pixel
BLACK_PIXEL = 250


def main():
    """
    在聖山中遇見神鹿
    """
    person = SimpleImage('image_contest/Shane.jpg')
    background = SimpleImage('image_contest/background.jpg')
    background.make_as_big_as(person)
    combined_img = combine(person, background)
    combined_img.show()


def combine(person, background):
    for x in range(person.width):
        for y in range(person.height):
            person_pixel = person.get_pixel(x, y)          # 人物原圖
            background_pixel = background.get_pixel(x, y)  # 背景原圖
            total = person_pixel.red + person_pixel.green + person_pixel.blue
            # 如果人物原圖中的平均數值小於灰色門檻且非黑色，用背景圖取代
            if -GRAY_PIXEL < total//3-person_pixel.red < GRAY_PIXEL and total > BLACK_PIXEL:
                person_pixel.red = background_pixel.red
                person_pixel.green = background_pixel.green
                person_pixel.blue = background_pixel.blue
    return person


if __name__ == '__main__':
    main()
