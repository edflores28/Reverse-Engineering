import copy
import constants

class Database:
    def __init__(self):
        '''
        Initialization
        '''
        self.database = []

    def insert(self, line):
        '''
        Inserts an instruction line to the database
        '''
        self.database.append(copy.deepcopy(line))

    def __parse_modrm_byte(self, byte):
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
    
    def __convert_displacement(self, displacement):
        displacement.reverse()
        hex_list = [hex(x) for x in displacement]
        hex_str = str(hex_list).replace(',','').replace('[','').replace(']','').replace(' ', '').replace('x','').replace('0','').replace("'",'')
        return hex_str.zfill(8)

    def __format_mod_rm_text(self, mod, reg, displacement):
        print(displacement)
        '''
        This routine formats the mod/rm byte
        '''
        register = constants.registers[reg]

        if displacement is not None:
            hex_disp = self.__convert_displacement(displacement)

        if mod is 3:
            return register
        if mod is 0:
            return '[' + register + ']'
        if mod is 2:
            return '[' + register + '+0x' + hex_disp + ']'

    def __determine_asm(self, opcode, mod, reg_op, rm, displacement=None):
        func = str(constants.opcodes[opcode])
        rega = None
        regb = None
        if displacement is None:
            rega = self.__format_mod_rm_text(mod, rm, None)
            regb = str(constants.registers[reg_op])
        else:
            rega = str(constants.registers[reg_op])
            regb = self.__format_mod_rm_text(mod, rm, displacement)

        return func + ' ' + rega + ' ' + regb

    def determine_no_modrm(self, line):
        '''
        This routine dissasemble opcodes with
        no mod/rm byte
        '''
        # Convert the opcode into binary
        opcode = line[0]
        binary = format(opcode, 'b')
        # Check for push instruction
        if constants.push_min <= opcode <= constants.push_max:
            return 'push ' + str(constants.registers[int(binary[4:8], 2)])
        # Check for pop instruction
        if constants.pop_min <= opcode <= constants.pop_max:
            return 'pop ' + str(constants.registers[int(binary[4:8], 2)])
        # Check for mov immediate instruction
        if constants.mov_min <= opcode <= constants.mov_max:
            return 'mov ' + str(constants.registers[int(binary[5:8], 2)] + ', 0x' + self.__convert_displacement(line[1:]))

    def __dissasemble(self, line):
        if len(line) == 1 or len(line) == 5:
            print("erer")
            # TODO Determine no modrm instructions here"
            print(self.determine_no_modrm(line))
            return

        mod, reg_op, rm = self.__parse_modrm_byte(line[1])
        displacement = None
        if line[0] is 0x8B:
            displacement = line[2:]
        print(self.__determine_asm(line[0], mod, reg_op, rm, displacement))

    def format(self):
        counts = [0 for i in range(len(self.database))]
        assembly = [None for i in range(len(self.database))]
        self.__dissasemble(self.database[8])
