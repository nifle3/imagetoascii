from typing import NoReturn
from os import path
import sys

from PIL import Image

def print_error(*args):
    print('\033[91mERROR: ', *args, '\033[39m')

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
        print(image.format, image.size, image.mode)
        image.show()

        


if __name__ == "__main__":
    main()
