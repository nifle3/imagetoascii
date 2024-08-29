from abc import ABC, abstractmethod

from PIL import Image
import numpy as np


class ASCIIConverter(ABC):
    @abstractmethod
    def __exit__(self):
        pass

    @abstractmethod
    def __enter__(self, exc_type, exc_val, exc_tb):
        pass

    @abstractmethod
    def convert(self) -> None:
        pass

class ASCIIBasicConverter(ASCIIConverter):
    __slots__ = ('image', 'width', 'heigth', 'scaling')
    
    def __init__(self, image: Image.Image, width: int | None, heigth: int | None, scaling: int):
        self.image = image
        self.width = width
        self.heigth = heigth
        self.scaling = scaling

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, exc_tb):
        self.image.close()

    def convert(self) -> None:
        image = self.image.convert('L')
        size = self._get_scale_size()
        
        image = image.resize(size)
        
        image_array = np.array(image)

        black = np.quantile(image_array, 1/3)
        for row in image_array:
            for pixel in row:
                char = ' '
                if pixel > black:
                    char = '#'

                print(char, end='')

            print('')

    def _get_scale_size(self) -> tuple[int]:
        width, heigth = self.image.size
        width = int(width / self.scaling)
        heigth = int(heigth / self.scaling)

        if self.width is not None:
            width = self.width
        
        if self.heigth is not None:
            heigth = self.heigth

        return (width, heigth)
