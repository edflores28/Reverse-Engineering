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
        self.raw_ins = copy.deepcopy(instruction)
        self.disp = None
        self.immediate = None
        self.ins_str = None
        self.kind = None
        # Determine if its an embedded opcode. If not parse
        # the mod/rm byte
        masked_code = instruction[0] & 0xF8
        if (masked_code not in constants.embed_opcodes) and (instruction[0] not in constants.ret_opcodes):
            self.mod, self.reg_op, self.rm = utilities.parse_modrm_byte(instruction[1])
        # Determine which dictionary the opcode and set
        # some parameters
        if instruction[0] in constants.opcodes:
            self.opcode = constants.opcodes[instruction[0]]
            self.kind = constants.Ins_Kind.REGULAR

        elif instruction[0] in constants.large_opcodes:
            self.opcode = constants.large_opcodes[instruction[0]][self.reg_op]
            self.kind = constants.Ins_Kind.LARGE
            # Check the mod byte and determine where to split
            # the list for displacement and immediate bytes
            if self.mod == 1:
                self.disp = copy.deepcopy(instruction[2])
                self.immediate = copy.deepcopy(instruction[3:])
            if self.mod == 2:
                self.disp = copy.deepcopy(instruction[2:6])
                self.immediate = copy.deepcopy(instruction[6:])

        elif instruction[0] in constants.disp_opcodes:
            self.opcode = constants.disp_opcodes[instruction[0]]
            self.disp = instruction[2:]
            self.kind = constants.Ins_Kind.DISPLACEMENT

        elif instruction[0] in constants.ret_opcodes:
            self.opcode = constants.ret_opcodes[instruction[0]]
            self.disp = instruction[1:]
            self.kind = constants.Ins_Kind.RETURN

        elif masked_code in constants.embed_opcodes:
            self.opcode = constants.embed_opcodes[masked_code]
            self.reg_op = instruction[0]&0x7 # Just place the register in reg_op
            self.kind = constants.Ins_Kind.EMBEDDED

        elif instruction[0] in constants.immed_opcode:
            self.opcode = constants.ret_opcodes[instruction[0]]
            self.immediate = instruction[1:]
            self.kind = constants.Ins_Kind.IMMEDIATE

    def get_opcode(self):
        return self.opcode

    def get_mod(self):
        return self.mod

    def get_reg_op(self):
        return self.reg_op

    def get_rm(self):
        return self.rm

    def get_raw_ins(self):
        self.raw_ins

    def get_disp(self):
        return self.disp  

    def get_kind(self):
        return self.kind
   
    def get_ins_str(self):
        return self.ins_str

    def get_immediate(self):
        return self.immediate

    def set_ins_str(self, line):
        self.ins_str = line

    def print(self):
        print(self.opcode, self.mod, self.reg_op, self.rm, self.raw_ins)