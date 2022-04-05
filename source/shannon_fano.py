import math
from utils import Utils

class ShannonFano:

    def __init__(self, input_path):
        """
        Constructor of the class
        """
        # initialize the utils class
        self.utils = Utils(input_path)
        # initialize the compression map and order list
        self.compression = {}
        self.decompression = {}
        self.order = []
        self.coded_text = ''
        self.decoded_text = ''

    def compress(self):
        """
        Compress the input text
        compression map structure:
            {'character': {'probability': Pr, 'lenght': Lsf, 'code': B2}}
        """
        print('Compressing...')
        # proccess the input text
        self.text = self.utils.get_text()
        self.lenght = len(self.text)
        self.frequency = self.utils.get_frequency()
        print(f'\nInput text:\n{self.text}\n')
        # compress the text
        self.get_basics()
        self.get_order()
        self.get_code()
        # print compression map
        [print(f'{repr(o[0])}:', self.compression[o[0]]) for o in self.order]
        # code the text
        self.get_coded_text()
        print(f'\nCompressed text:\n{self.coded_text}\n')
        # decompression map
        self.get_decode()
        # print the decompression map
        [print(f'{key}:', value) for key, value in self.decompression.items()]
        # decode the text
        self.get_decoded_text()
        print(f'\nDecompressed text:\n{self.decoded_text}')

    def get_basics(self):
        """
        Calculate the probability and lenght of each character
        """
        for char in self.frequency:
            frequency = self.frequency[char]
            probability = frequency / self.lenght
            lenght = math.ceil(math.log(1 / probability, 2)) if probability != 1 else 1
            self.compression[char] = {'probability': probability, 'lenght': lenght, 'frequency': frequency}

    def get_order(self):
        """
        Get the order of the characters by descending probability
        """
        for char in self.compression:
            probability = self.compression[char]['probability']
            self.order.append([char, probability])
        self.order.sort(key=lambda x: x[1], reverse=True)

    def get_code(self):
        """
        Get the code of each character
        """
        # base case for the first character
        char = self.order[0][0]
        self.compression[char]['code'] = '0' * self.compression[char]['lenght']
        # iterate over the rest of the characters
        for i in range(1, len(self.order)):
            # calculate the current char and lenght
            char = self.order[i][0]
            lenght = self.compression[char]['lenght']
            # calculate the previous char, lenght and code
            prev_char = self.order[i-1][0]
            prev_lenght = self.compression[prev_char]['lenght']
            prev_code = self.compression[prev_char]['code']
            # calculate the code of the current char
            d = lenght - prev_lenght
            code = self.utils.binary_multiply(self.utils.binary_add(prev_code, '1'), bin(2**d)[2:])
            self.compression[char]['code'] = self.utils.fill_zeros(code, lenght)

    def get_coded_text(self):
        """
        Get the coded text
        """
        for char in self.text:
            self.coded_text += self.compression[char]['code']
    
    def get_decode(self):
        """
        Get the uncoded text
        """
        for char in self.compression:
            code = self.compression[char]['code']
            self.decompression[code] = {
                'probability': self.compression[char]['probability'], 
                'lenght': self.compression[char]['lenght'], 
                'frequency': self.compression[char]['frequency'],
                'char': char
            }
    
    def get_decoded_text(self):
        """
        Get the decoded text
        """
        text = ''
        for item in self.coded_text:
            text += item
            char = self.decompression.get(text)
            if char:
                letter = char['char']
                self.decoded_text += letter
                text = ''



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
