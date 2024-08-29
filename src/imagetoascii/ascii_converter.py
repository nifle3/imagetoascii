from abc import ABC, abstractmethod

from PIL import Image

class ASCIIConverter(ABC):
    @abstractmethod
    def __exit__(self):
        pass

    @abstractmethod
    def __enter__(self, exc_type, exc_val, exc_tb):
        pass

class ASCIIBasicConverter(ASCIIConverter):
    __slots__ = ('image', 'width', 'heigth', 'scaling')
    
    def __init__(self, image: Image.Image, width: int, heigth: int, scaling: int):
        self.image = image
        self.width = width
        self.heigth = heigth
        self.scaling = scaling

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, exc_tb):
        self.image.close()