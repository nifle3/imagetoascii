from typing import NoReturn
from os import path
import sys
import optparse

from PIL import Image
import numpy as np

def main() -> NoReturn:
    args = sys.argv
    if len(args) < 2:
        print_error('Enter a path to image')
        sys.exit(1)

    file_path = args[1]
    if not path.exists(file_path):
        print_error('Enter a valid file path')
        sys.exit(1)

    with Image.open(file_path)as image:
        image = image.convert('L')
        width, heigth = image.size
        image = image.resize(get_scale_size(width, heigth))

        image_array = np.array(image)

        black = np.quantile(image_array, 1/3)

        for row in image_array:
            for pixel in row:
                char = ' '
                if pixel > black:
                    char = '#'

                print(char, end='')

            print('')


def print_error(*args):
    print('\033[91mERROR: ', *args, '\033[39m')


def get_scale_size(width: int, heigth: int) -> tuple[int]:
    scale = 10

    return (int(width / scale), int(heigth / scale))


if __name__ == "__main__":
    parser_opts = optparse.OptionParser()
    parser_opts.add_option('--url', '-U', help='Set url, that download image (network requirement)',)
    parser_opts.add_option('--width', '-W', help='Set width of final picture')
    parser_opts.add_option('--heigth', '-H', help='Set heigth of final picture')
    parser_opts.add_option('--scaling', '-S', help='Set scaling of sizing picture (overwrite with -w and -h)')

    (option, args) = parser_opts.parse_args()
    #main()
