import constants

def parse_modrm_byte(byte):
    '''
    This routine decipohers the mod/rm byte
    '''
    # Convert the byte into binary
    binary = format(byte, 'b')
    # Split the binary string and convert
    # the values back into integers
    mod = int(binary[:2], 2)
    reg_op = int(binary[2:5],2)
    rm = int(binary[5:8],2)
    return mod, reg_op, rm

def valid_opcode(byte):
    '''
    Checks to see if the byte is a valid opcode
    '''
    if byte in constants.opcodes:
        return True
    if byte in constants.disp_opcodes:
        return True
    if byte in constants.large_opcodes:
        return True
    if byte in constants.ret_opcodes:
        return True
    # Check to see if the instructed is offsetted
    mask = byte & 0xF8
    if mask in constants.embed_opcodes:
        return True
    return False