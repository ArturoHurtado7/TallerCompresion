import math

class Utils:

    def __init__(self, input_path=''):
        if input_path: self.input = self.read_input(input_path)

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

    def get_bit_size(self, input):
        """
        Get the byte size of the input text
        """
        return len(input.encode('utf-16'))*8

    def get_frequency(self):
        """
        Get the frequency of each character
        """
        self.frequency = {}
        for char in self.input:
            if char in self.frequency:
                self.frequency[char] += 1
            else:
                self.frequency[char] = 1
        return self.frequency

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

    def get_encode_value(self, binary_text):
        """
        Get the encode value
        """
        return bin(int(binary_text, 2)).encode('utf-8')

    def worse_case_entropy(self):
        """
        Calculate the worse case entropy
        """
        return math.log(len(self.frequency),2)

    def export_file(self, source, output_path):
        """
        export  file
        """
        try: 
            with open(output_path, 'w', encoding='utf-8', newline='') as f:
                f.write(source)
            return f'\nArchivo de estadisticas "{output_path}" exportado satisfactoriamente\n'
        except Exception as e:
            print(f'Error: file "{output_path}" {e}')
            exit(1)

    def export_binary(self, source, output_path):
        """
        export binary file
        """
        try:
            with open(output_path, 'wb') as f:
                f.write(source)
            return f'\nArchivo Binario "{output_path}" exportado satisfactoriamente'
        except Exception as e:
            print(f'Error: file "{output_path}" {e}')
            exit(1)
