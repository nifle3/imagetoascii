from typing import Final
import re
import requests
from os import path
from io import BytesIO


from PIL import Image

from errors import InvalidState
from ascii_converter import ASCIIConverter, ASCIIBasicConverter


class ASCIIConverterBuilder:
    __slots__ = ('image_path', 'image_url', 'width', 'heigth', 'scaling')

    URL_PATTERN: Final[str] = '^[-a-zA-Z0-9@:%._\\+~#=]{1,256}\\.[a-zA-Z0-9()]{1,6}\\b(?:[-a-zA-Z0-9()@:%_\\+.~#?&\\/=]*)$'
    
    def __init__(self):
        self.image_path = None
        self.image_url = None
        self.width = None
        self.heigth = None
        self.scaling = 30

    def set_image_path(self, image_path: str):
        if self.image_url is not None:
            raise InvalidState('You already set an image url')

        if not path.exists(image_path):
            raise ValueError('Enter a valid file path')

        self.image_path = image_path
        return self

    def set_image_url(self, url: str):
        if self.image_path is not None:
            raise InvalidState('You already set an image path')

        if not re.match(url, self.URL_PATTERN):
            raise ValueError('You enter an invalid url')

        self.image_url = url
        return self

    def set_width(self, width: str):
        if not width.isdigit():
            raise ValueError('Width must be int')

        if int(width) < 0:
            raise ValueError('Width must be greater than zero')

        self.width = int(width)
        return self

    def set_heigth(self, heigth: str):
        if not heigth.isdigit():
            raise ValueError('Heigth must be int')

        if int(heigth) < 0:
            raise ValueError('Heigth must be greater than zero')

        self.heigth = int(heigth)
        return self

    def set_scaling(self, scale: str):
        if not scale.isdigit():
            raise ValueError('Scale must be int')

        if int(scale) < 0:
            raise ValueError('Scaling must be greater than zero')
        
        self.scaling = int(scale)
        return self

    def build(self) -> ASCIIConverter:
        if self.image_path is None and self.image_url is None:
            raise InvalidState('You must enter image path or image_url')
        
        if self.image_path is not None:
            image = Image.open(self.image_path)
        elif self.image_url is not None:
            response = requests.get(self.image_url)
            byte_buffer = BytesIO(response.content)
            image = Image.open(byte_buffer)
        
        return ASCIIBasicConverter(image, self.width, self.heigth, self.scaling)
