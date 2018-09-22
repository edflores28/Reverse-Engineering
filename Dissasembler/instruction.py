import constants
import copy
import utilities

class Set:
    def __init__(self, instruction):
        '''
        Initialization
        '''
        self.opcode = None
        self.mod = None
        self.reg_op = None
        self.rm = None
        self.raw = copy.deepcopy(instruction)
        self.disp = None
        self.immediate = None
        self.ins_str = None
        self.kind = None
        self.en = None
        self.is_jmp = False
        self.bytes = None
        # if instruction is none, return
        if not instruction:
            return
        # Set the bytes
        self.bytes = len(instruction)
        # Find out the encoding.
        try:
            self.en = constants.opcodes[self.raw[0]][0]
        except KeyError:
             # Check to see if the masked encoding exists
            try:
                self.en = constants.opcodes[(instruction[0]&0xF8)][0]
            except KeyError:
                # Keep it to none. Invalid opcode
                self.en = None

        # Get mod/rm byte if necessary
        if utilities.determine_parse(self.en):
            self.mod, self.reg_op, self.rm = utilities.parse_modrm_byte(instruction[1])
        # Set the values according to the opcode encoding
        if self.en is 'o':
            self.opcode = constants.opcodes[(instruction[0]&0xF8)][1]
            self.reg_op = instruction[0]&0x7

        elif self.en is 'i':
            self.opcode = constants.opcodes[instruction[0]][1]
            self.immediate = instruction[1:5]

        elif self.en is 'oi':
            self.opcode = constants.opcodes[(instruction[0]&0xF8)][1]
            self.reg_op = instruction[0]&0x7
            self.immediate = instruction[1:5]   

        elif self.en is 'mi':
            self.opcode = constants.opcodes[instruction[0]][1][self.reg_op]
            self.__set_disp_immd(self.mod, instruction)
            
        elif self.en is 'm1':
            self.opcode = constants.opcodes[instruction[0]][1][self.reg_op]

        elif self.en is 'rm' or self.en is 'mr':
            self.opcode = constants.opcodes[instruction[0]][1]
            self.__set_disp_immd(self.mod, instruction)

        elif self.en is 'zo':
            self.opcode = constants.opcodes[instruction[0]][1]

        elif self.en is 'd':
            self.is_jmp = True
            self.opcode = constants.opcodes[instruction[0]][1]
            self.offset = utilities.convert_address(instruction[1:])
            self.dec_addr = int(self.offset, 16)

    def __set_disp_immd(self, mod, instruction):
        '''
        Determines the displacement and immediate parameters
        '''
        offset = utilities.determine_list_size(self.mod)+2
        self.disp = instruction[2: offset]
        self.immediate = instruction[offset: offset+4]

    def get_opcode(self):
        return self.opcode

    def get_mod(self):
        return self.mod

    def get_reg_op(self):
        return self.reg_op

    def get_rm(self):
        return self.rm

    def get_disp(self):
        return self.disp  

    def get_kind(self):
        return self.kind
   
    def get_ins_str(self):
        return self.ins_str

    def get_immediate(self):
        return self.immediate

    def get_en(self):
        return self.en

    def get_offset(self):
        return self.offset
    
    def get_is_jmp(self):
        return self.is_jmp
    
    def get_raw(self):
        return self.raw

    def get_bytes(self):
        return self.bytes

    def set_ins_str(self, line):
        self.ins_str = line

    def get_dec_addr(self):
        return self.dec_addr

    def print(self):
        print(self.opcode, self.mod, self.reg_op, self.rm)