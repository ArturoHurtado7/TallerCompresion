import json
from utils import Utils

class Huffman:

    def __init__(self, input_path):
        """
        Constructor of the class
        """
        # initialize the utils class
        self.utils = Utils(input_path)

        # initialize the compression map and order list
        self.compression_map = {}
        self.compression = {}
        self.decompression = {}
        self.order = []
        self.coded_text = ''
        self.decoded_text = ''
        self.id = 0

    def compress(self):
        """
        Compress the input text
        compression map structure:
            {'id': {'char': char, 'weight': weight, 'father_node': father_node, 'code': code}}
        """

        # proccess the input text
        self.text = self.utils.get_text()
        self.lenght = len(self.text)
        self.frequency = self.utils.get_frequency()

        # Get the compression map and the order list
        self.get_basics()

        # Get the tree iteratively over the order list
        while len(self.order) > 1:
            self.order_tree()

        # Get the compression codes from the buttom to the top
        self.get_compression_codes()
        [print(f'compression: {c}') for c in self.compression.items()]
        
        # Get the coded text
        self.get_coded_text()
        print(f'\nCompressed text:\n{self.coded_text}\n')
        self.get_decoded_text()
        [print(f'decompression: {c}') for c in self.decompression.items()]
        print(f'\nDecompressed text:\n{self.decoded_text}\n')

        # get the stats
        stats = self.get_stats()
        print(stats)
        return self.utils.get_encode_value(self.coded_text), stats

    def get_basics(self):
        """
        Calculate the compression map and order list by the frequency for the first time
        """
        for char, frequency in self.frequency.items():
            id = self.get_id()
            self.compression_map[id] = {'char': char, 'weight': frequency, 'father_node': None, 'code': None}
            self.order.append([id, frequency])
        self.order.sort(key=lambda x: x[1])

    def order_tree(self):
        """
        Get the tree by order of order list
        """

        # get the father node attributes
        left_item = self.order[0][0]
        right_item = self.order[1][0]
        weight = self.order[0][1] + self.order[1][1]
        father_node = self.get_id()

        # extract the two smallest nodes
        self.order.pop(0)
        self.order.pop(0)

        # add the father node to the compression map
        self.compression_map[father_node] = {'char': None, 'weight': weight, 'father_node': None, 'code': None}

        # update the left and right nodes
        self.compression_map[left_item]['father_node'] = father_node
        self.compression_map[left_item]['code'] = '0'
        self.compression_map[right_item]['father_node'] = father_node
        self.compression_map[right_item]['code'] = '1'

        # add the father node to the order list
        self.order.append([father_node, weight])
        self.order.sort(key=lambda x: x[1])

    def get_compression_codes(self):
        """
        Get the compression by the coded text.
        hiking the compression map from bottom to top.
        """

        # start from the first node
        i = 1 
        char = self.compression_map[i]['char']

        # iterate over the compression map only for the nodes with chars
        while char:
            # starting point variables
            code = self.compression_map[i]['code']
            father_node = self.compression_map[i]['father_node']

            # get code from the bottom to the top
            while self.compression_map[father_node]['code']:
                code = self.compression_map[father_node]['code'] + code
                father_node = self.compression_map[father_node]['father_node']

            # add the code to the compression result dictionary
            self.compression[char] = code
            self.decompression[code] = char

            # next iteration
            i += 1
            char = self.compression_map[i]['char']

    def get_id(self):
        """
        Get the next id for the compression map and return it
        """
        self.id += 1
        return self.id

    def get_coded_text(self):
        """
        Get the coded text
        """
        for char in self.text:
            self.coded_text += self.compression[char]

    def get_decoded_text(self):
        """
        Get the decoded text
        """
        text = ''
        for item in self.coded_text:
            text += item
            char = self.decompression.get(text)
            if char:
                self.decoded_text += char
                text = ''

    def get_stats(self):
        """
        Get the compression stats
        """
        stats = 'Stats Huffman:\n'
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
            expected_bits += probability * len(self.compression[char])
        return expected_bits
