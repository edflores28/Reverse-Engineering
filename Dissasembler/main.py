import argparse
import os.path

def open_file(parse, file):
    '''
    Routine that opens a file for reading if
    it exists.
    '''
    if not os.path.exists(file):
        parser.error("Invalid file: " + file)
    else:
        return open(file, 'rb')

# Create a parser for the binary file
parser = argparse.ArgumentParser(description="Dissasembler")
parser.add_argument("-f", dest="filename", required=True, help="Machine code file", type=lambda x: open_file(parser, x))

# Read user inputs
args = parser.parse_args()

while True:
    current_byte = args.filename.read(1)
    if not current_byte:
        break
    val = ord(current_byte)
    print(val)
    print("%#5X"% (val))
