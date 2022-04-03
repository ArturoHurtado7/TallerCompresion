from utils import Utils

class Huffman:

    def __init__(self, input_path):
        self.utils = Utils(input_path)
        self.text = self.utils.get_text()
        self.frequency = self.utils.get_frequency()

    def compress(self):
        print('Compressing...')
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

