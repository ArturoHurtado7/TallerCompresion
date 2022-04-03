
class Utils:

    def __init__(self, input_path):
        self.input = self.read_input(input_path)

    def read_input(self, input_path):
        """
        Read the input file
        """
        try:
            with open(input_path, 'r', encoding="utf-8") as f:
                return f.read()
        except FileNotFoundError:
            print(f'Error: file "{input_path}" not found')
            exit(1)

    def get_text(self):
        """
        Get the input text
        """
        return self.input
    
    def get_byte_size(self, input):
        """
        Get the byte size of the input text
        """
        return len(input.encode('utf-8'))

    def get_frequency(self):
        """
        Get the frequency of each character
        """
        frequency = {}
        for char in self.input:
            if char in frequency:
                frequency[char] += 1
            else:
                frequency[char] = 1
        return frequency

    def get_ascii(self, input):
        """
        Get the ascii value
        """
        return ord(input)

    def get_char(self, input):
        """
        Get the char value
        """
        return chr(input)

    def binary_add(self, a, b):
        """
        Add two binary strings
        """
        return bin(int(a, 2) + int(b, 2))[2:]

    def binary_multiply(self, a, b):
        """
        Multiply two binary strings
        """
        return bin(int(a, 2) * int(b, 2))[2:]
    
    def fill_zeros(self, binary, lenght):
        """
        Fill the binary string with zeros
        """
        return '0' * (lenght - len(binary)) + binary