from typing import NoReturn
import sys

from ascii_converter_builder import ASCIIConverterBuilder
from cli import CLI

"""
#def main() -> NoReturn:
    with Image.open(file_path)as image:
        
"""

def main() -> NoReturn:
    cli = CLI()

    try:
        cli.parse()
        image_place = cli.image_path
        option = cli.option

        builder = ASCIIConverterBuilder()
        if option.url:
            builder.set_image_url(image_place)
        else:
            builder.set_image_path(image_place)

        if option.width is not None:
            builder.set_width(option.width)
        
        if option.heigth is not None:
            builder.set_heigth(option.heigth)

        if option.scaling is not None:
            builder.set_scaling(option.scaling)

        with builder.build() as converter:
            converter.convert()

    except Exception as e:
        print_error(e)
        sys.exit(1)


def print_error(*args):
    print('\033[91mERROR: ', *args, '\033[39m')


def get_scale_size(width: int, heigth: int) -> tuple[int]:
    scale = 10

    return (int(width / scale), int(heigth / scale))


if __name__ == "__main__":
    main()
