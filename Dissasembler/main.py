import argparse
import os.path
import database
import constants
import utilities
import instruction
def open_file(parse, file):
    '''
    Routine that opens a file for reading if
    it exists.
    '''
    if not os.path.exists(file):
        parser.error("Invalid file: " + file)
    else:
        return open(file, 'rb')

def create_and_insert(line, database):
    # Make sure to handle any errors
    try:
        instr = instruction.Set(line)
    except:
        instr = instruction.Set(None)
    database.insert(instr)
    line.clear()
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
prev_enc = None
while True:
    current_byte = args.filename.read(1)
    try:
        val = ord(current_byte)
    except TypeError:
        create_and_insert(line, machine_code)
        break
    valid, encode = utilities.valid_opcode(val)
    if valid:
        # If the list list empty add the valid opcode
        if not prev_enc:
            prev_enc = encode
        # Lets check the encoding
        else:
            # If the current opcode is 'o' or 'zo'
            # then we have built the current insruction
            if  prev_enc is 'o' or prev_enc is 'zo':
                prev_enc = encode
                create_and_insert(line, machine_code)
            # Look at the opcodes that use memory
            elif len(line) >= 2 and 'm' in prev_enc:
                mod, reg_op, rm = utilities.parse_modrm_byte(line[1])
                size = utilities.determine_list_size(mod)
                # increment the size by 4 if the opcode is 'mi'
                if prev_enc is 'mi':
                    size += 4
                if len(line) == (size+2):
                    prev_enc = encode
                    create_and_insert(line, machine_code)
            elif len(line) == 5 and (prev_enc is 'i' or  prev_enc is 'oi'):
                    prev_enc = encode
                    create_and_insert(line, machine_code)
            elif prev_enc is 'd' and (len(line) == 2 or len(line) == 5):
                    prev_enc = encode
                    create_and_insert(line, machine_code)

    # Add the byte to the line
    line.append(val)

machine_code.dissasemble_database()