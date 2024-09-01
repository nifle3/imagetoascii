from optparse import OptionParser

class CLI:
    __slots__ = ('parser', 'image_path', 'option')

    def __init__(self) -> None:
        self.image_path = None
        self.option = None

        self.parser = OptionParser()
        self.parser.add_option('--url', '-U', help='Set that path is url, that download image (network requirement)', 
            default=False,  action = 'store_true')
        self.parser.add_option('--width', '-W', help='Set width of final picture')
        self.parser.add_option('--heigth', '-H', help='Set heigth of final picture')
        self.parser.add_option('--scaling', '-S', help='Set scaling of sizing picture (overwrite with -w and -h)')

    def parse(self) -> None:
        (option, args) = self.parser.parse_args()

        if len(args) < 1:
            raise ValueError('Enter a path to image')

        self.image_path = args[0]
        self.option = option