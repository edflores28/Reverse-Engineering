import constants

def parse_modrm_byte(byte):
    '''
    This routine decipohers the mod/rm byte
    '''
    # Convert the byte into binary
    binary = format(byte, 'b').zfill(8)

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
        return True, constants.opcodes[byte][0]
    masked = byte&0xF8
    if masked in constants.opcodes:
         return True, constants.opcodes[masked][0]
    return False, None

def determine_parse(en):
    if 'm' in en:
        return True
    return False

def determine_list_size(mod):
    if mod is 1:
        return 1
    if mod is 2:
        return 4
    return 0

def convert_address(address, reverse=True):
    if address is not None:
        if reverse:
            address.reverse()
        hex_list = [hex(x) for x in address]
        hex_str = str(hex_list).replace(',','').replace('[','').replace(']','').replace(' ', '').replace('x','').replace('0','').replace("'",'')
        return '0x' + hex_str.zfill(len(address)*2)
    return ''