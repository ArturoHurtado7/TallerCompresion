import math
import json
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
        self.get_code()
        
        # print compression map
        [print(f'compression: {repr(o[0])}:', self.compression[o[0]]) for o in self.order]
        
        # code the text
        self.get_coded_text()
        print(f'\nCompressed text:\n{self.coded_text}\n')
        
        # decompression map
        self.get_decode()
        
        # print the decompression map
        [print(f'decompression: {key}:', value) for key, value in self.decompression.items()]
        
        # decode the text
        self.get_decoded_text()
        print(f'\nDecompressed text:\n{self.decoded_text}\n')
        
        # Get the stats
        stats = self.get_stats()
        print(stats)
        return self.utils.get_encode_value(self.coded_text), stats


    def get_basics(self):
        """
        Calculate the probability and lenght of each character
        """
        for char in self.frequency:
            frequency = self.frequency[char]
            probability = frequency / self.lenght
            lenght = math.ceil(math.log(1 / probability, 2)) if probability != 1 else 1
            self.compression[char] = {'probability': probability, 'lenght': lenght, 'frequency': frequency}
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
            code = self.utils.fill_zeros(code, lenght)
            self.compression[char]['code'] = code


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


    def get_stats(self):
        """
        Get the stats
        """
        stats = 'Stats Shanno Fano:\n'
        stats += f'Original bits length: {self.utils.get_bit_size(self.text)}\n'
        stats += f'Compressed bits length: {len(self.coded_text)}\n'
        stats += f'Expected bits number per character: {self.expected_bits()}\n'
        stats += f'Worse case entropy: {self.utils.worse_case_entropy()}\n'
        stats += str(json.dumps(self.decompression, indent=4, sort_keys=True))
        return stats


    def expected_bits(self):
        """
        Calculate the expected bits
        """
        expected_bits = 0
        for char in self.compression:
            probability = self.frequency[char] / self.lenght
            expected_bits += probability * len(self.compression[char]['code'])
        return expected_bits
