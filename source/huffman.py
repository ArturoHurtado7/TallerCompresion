from utils import Utils

class Huffman:

    def __init__(self, input_path):
        # initialize the utils class
        self.utils = Utils(input_path)
        # initialize the compression map and order list
        self.compression = {}
        self.decompression = {}
        self.order = []
        self.coded_text = ''
        self.decoded_text = ''

    def compress(self):
        print('Compressing...')
        self.text = self.utils.get_text()
        self.lenght = len(self.text)
        self.frequency = self.utils.get_frequency()
        print(f'Frequency: {self.frequency}')

    def decompress(self):
        print('Decompressing...')

    def code_table(self):
        print('Generating code table...')

    def expected_bits(self):
        print('Calculating expected bits...')

    def worse_case_entropy(self):
        print('Calculating worse case entropy...')

    def total_bits(self):
        print('Calculating total bits...')

