import sys
from huffman import Huffman
from shannon_fano import ShannonFano

# input arguments
args = sys.argv[1:]

# global varibles
input_path = output_path = compression = action = None

# valid compression and actions
compressions = ['huffman', 'shannon_fano']
actions = ['compress', 'decompress']


def help():
    """
    Prints help messages
    """
    print('\nUsage:\n')
    print('> python main.py <compression> [compression] <action> [action] <input> [input] <output> [output]\n')

    print('valid arguments:\n')
    print(' <compression>: \t -c or --compression')
    print(' <action>: \t\t -a or --action')
    print(' <input>: \t\t -i or --input')
    print(' <output>: \t\t -o or --output\n')

    print('valid options:\n')
    print(f' [compressions]: \t {" OR ".join(compressions)}')
    print(f' [actions]: \t\t {" OR ".join(actions)}')
    print(f' [input]: \t\t path in machine')
    print(f' [output]: \t\t path in machine \n')

    print('Examples:\n')
    print('> python main.py -c huffman -a compress -i C:\input.txt -o C:\output.txt')
    print('> python main.py --compression huffman --action compress --input C:\input.txt --output C:\output.txt\n')
    exit(1)


def main():
    """
    Main function, parses arguments and calls the correct class
    """

    # check if the user needs help
    if any(e in ['-h', '--help'] for e in args): help()

    # check if ammount of arguments is correct
    if len(args) % 2 != 0:
        print('Error: wrong number of arguments, use -h or --help for help')
        exit(1)

    # check if parameters are valid, iterate over args by 2
    for i in range(0, len(args), 2):
        if args[i] in ['-i', '--input']:
            input_path = args[i+1]
        elif args[i] in ['-o', '--output']:
            output_path = args[i+1]
        elif args[i] in ['-c', '--compression']:
            compression = args[i+1]
            if compression not in compressions:
                print(f'Error: compression "{compression}" invalid ')
                print(f'Valid compressions: {" ".join(compressions)}')
                exit(1)
        elif args[i] in ['-a', '--action']:
            action = args[i+1]
            if action not in actions:
                print(f'Error: action "{action}" invalid ')
                print(f'Valid actions: {" ".join(actions)}')
                exit(1)
        else:
            print(f'Error: parameter "{args[i]}" invalid')
            exit(1)
    if not input_path or not output_path or not compression or not action:
        print('Error: missing parameters, use -h or --help for help')        
        exit(1)


    # call the correct compression and action
    if compression == 'huffman':
        compressor = Huffman(input_path)
    elif compression == 'shannon_fano':
        compressor = ShannonFano(input_path)

    if action == 'compress':
        compressor.compress()
    elif action == 'decompress':
        compressor.decompress()

# call main
if __name__ == "__main__":
    main()

