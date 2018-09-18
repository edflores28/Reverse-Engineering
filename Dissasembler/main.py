import argparse
import os.path
import database
import constants

def open_file(parse, file):
    '''
    Routine that opens a file for reading if
    it exists.
    '''
    if not os.path.exists(file):
        parser.error("Invalid file: " + file)
    else:
        return open(file, 'rb')

'''
Main application
'''
# Create a parser for the binary file
parser = argparse.ArgumentParser(description="Dissasembler")
parser.add_argument("-f", dest="filename", required=True, help="Machine code file", type=lambda x: open_file(parser, x))

# Read user inputs
args = parser.parse_args()

# Instantiate the database
machine_code = database.Database()
line = []
found_opcode = False
while True:
    current_byte = args.filename.read(1)
    try:
        val = ord(current_byte)
    except TypeError:
        print("Error")
        machine_code.insert(line)
        break
    if val in constants.opcodes:
        # If there are bytes in the line then
        # insert the list in the database
        # and clear the line list
        if len(line) > 0:
            #print(hex(line))
            machine_code.insert(line)
            line.clear()
    # Add the byte to the line
    line.append(val)

machine_code.format()