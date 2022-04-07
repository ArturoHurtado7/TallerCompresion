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
        self.left  = None
        self.right = None
        self.huff = ''


    def compress(self):
        print('Compressing...')
        self.text = self.utils.get_text()
        self.lenght = len(self.text)
        self.frequency = self.utils.get_frequency()
        data = {key: value for key, value in sorted(self.frequency.items(), key=lambda item: item[1])}
        list = [(key, value) for key, value in data.items()]
        print(list)
        while len(list) > 1 :
            leastTwo = tuple(list[0:2])                  
            theRest  = list[2:]                          
            combFreq = leastTwo[0][0] + leastTwo[1][0]     
            list   = theRest + [(combFreq,leastTwo)]     
            list.sort()
        print(list)
        

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

