from sys import maxsize as maxs
from colorama import Fore,init
init()

digits = [line.rstrip('\n') for line in open('p8.txt')][0]
# Image is 25 pixels wide and 6 pixels tall, 150 digits in total
image_size = 25 * 6
num_of_images = int(len(digits)/image_size)
images = []
min_zeroes = maxs
for image in range(num_of_images):
    pixels = digits[image*image_size:(image+1)*image_size]
    images.append(pixels)
    """ Part 1
    zeroes = pixels.count('0')
    if zeroes < min_zeroes:
        min_zeroes = zeroes
        result = pixels.count('1') * pixels.count('2')
    """
# Part 2
# 0 -> black / 1 -> white / 2 -> transparent
# Check same pixel of each layer
result = []
for pixel in range(image_size):
    layer = 0
    while images[layer][pixel] == '2':
        layer += 1
    result.append(images[layer][pixel])
result = ''.join(result)
# Print the message clearly with color
for row in range(6):
    for column in range(25):
        if result[column+row*25] == '1':
            print(Fore.GREEN + result[column+row*25],end='')
        else:
            print(Fore.WHITE + result[column+row*25],end='')
    print('')
