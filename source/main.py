import sys
from huffman import Huffman
from shannon_fano import ShannonFano
from utils import Utils

# input arguments
args = sys.argv[1:]

# global varibles
input_path = output_path = stats_path = compression = action = None

# valid compression and actions
compressions = ['huffman', 'shannon_fano']


def help():
    """
    Prints help messages
    """
    print('\nUsage:\n')
    print('> python main.py <compression> [compression] <input> [input]\n')

    print('valid arguments:\n')
    print(' <compression>: \t -c or --compression')
    print(' <input>: \t\t -i or --input\n')

    print('valid options:\n')
    print(f' [compressions]: \t {" OR ".join(compressions)}')
    print(f' [input]: \t\t path in machine\n')

    print('Examples:\n')
    print('> python main.py -c huffman -a compress -i "C:\input.txt"')
    print('> python main.py --compression huffman --input "C:\input.txt"\n')
    print('> python main.py -c shannon_fano -a compress -i "C:\input.txt"')
    print('> python main.py --compression shannon_fano --input "C:\input.txt"\n')
    exit(1)


def main():
    """
    Main function, parses arguments and calls the correct class
    """

    # check if the user needs help
    if any(e in ['-h', '--help'] for e in args): help()

    # check if ammount of arguments is even
    if len(args) % 2 != 0:
        print('Error: wrong number of arguments, use -h or --help for help')
        exit(1)

    # check if parameters are valid, iterate over even args
    for i in range(0, len(args), 2):
        if args[i] in ['-i', '--input']:
            input_path = args[i+1]
            output_path = input_path.replace('.txt', '_comp.bin')
            stats_path = input_path.replace('.txt', '_stats.txt')
        elif args[i] in ['-c', '--compression']:
            compression = args[i+1]
            if compression not in compressions:
                print(f'Error: compression "{compression}" invalid ')
                print(f'Valid compressions: {" ".join(compressions)}')
                exit(1)
        else:
            print(f'Error: parameter "{args[i]}" invalid')
            exit(1)
    if not input_path or not output_path or not stats_path or not compression:
        print('Error: missing parameters, use -h or --help for help')        
        exit(1)

    # call the correct compression
    if compression == 'huffman':
        compressor = Huffman(input_path)
    elif compression == 'shannon_fano':
        compressor = ShannonFano(input_path)

    # compress file
    coded, stats = compressor.compress()

    # export stats and binary file
    util = Utils()
    print(util.export_binary(source=coded, output_path=output_path))
    print(util.export_file(source=stats, output_path=stats_path))


# main function call
if __name__ == "__main__":
    main()

