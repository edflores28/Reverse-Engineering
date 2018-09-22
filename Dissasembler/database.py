import copy
import constants
import utilities

class Database:
    def __init__(self):
        '''
        Initialization
        '''
        self.database = []

    def insert(self, instruction):
        '''
        Inserts an instruction to the database
        '''
        self.database.append(copy.deepcopy(instruction))

    def __format_mod_rm_text(self, mod, rm, displacement):
        '''
        This routine formats the mod/rm byte
        '''
        register = constants.registers[rm]
        if displacement is not None:
            hex_disp = utilities.convert_address(displacement)
        if mod is 3:
            return register
        if mod is 0:
            return '[' + register + ']'
        if mod is 2 or mod is 1:
            return '[' + register + '+' + hex_disp + ']'

    def __process(self, item):
        '''
        Iterate through the item and set necessary values
        '''
        if item.get_en() is None:
            return
        rega = ''
        regb = ''
        if item.get_en() is 'mr':
            rega = self.__format_mod_rm_text(item.get_mod(), item.get_rm(), item.get_disp()) + ', '
            regb = str(constants.registers[item.get_reg_op()])
        
        if item.get_en() is 'mi':
            rega = self.__format_mod_rm_text(item.get_mod(), item.get_rm(), item.get_disp()) + ', '
            regb = utilities.convert_address(item.get_immediate())

        if item.get_en() is 'm1':
            rega = self.__format_mod_rm_text(item.get_mod(), item.get_rm(), item.get_disp()) + ', '
            regb = '1'

        if item.get_en() is 'rm':
            regb = self.__format_mod_rm_text(item.get_mod(), item.get_rm(), item.get_disp())
            rega = str(constants.registers[item.get_reg_op()]) + ', '

        if item.get_en() is 'i':
            immd = utilities.convert_address(item.get_immediate())
            # Set rega and regb if it's 'out'
            if item.get_opcode() is 'out':
                rega = immd + ', '
                regb = 'eax'
            else:
                rega = 'eax, '
                regb = immd

        if item.get_en() is 'o':
            rega = str(constants.registers[item.get_reg_op()])
            regb = ''

        if item.get_en() is 'oi':
            rega = str(constants.registers[item.get_reg_op()]) + ', '
            regb = utilities.convert_address(item.get_immediate())

        if item.get_en() is 'd':
            rega = 'offset_' + item.get_offset() + 'h'
            regb = ''     
        item.set_ins_str(rega + regb)
    
    #def conv_raw(raw):

    def dissasemble_database(self):
        address_list = []
        byte_counter = 0
        jump_addrs = {}
        # Iterate through the entire database and process is
        for ins in self.database:
            self.__process(ins)
            size = ins.get_bytes()
            if size is not None:
                address_list.append(byte_counter)
                byte_counter += ins.get_bytes()
                if ins.get_is_jmp():
                    jump_addrs[ins.get_dec_addr()] = ins.get_offset()
            # For invalid opcodes increment the counter by 1
            else:
                byte_counter += 1
        # Iterate through the database and print out the dissasembly
        for item in range(len(self.database)):
            if self.database[item].get_bytes() is not None:
                hex_str = hex(address_list[item]).replace('x','').zfill(8)
                instruction = utilities.convert_address(self.database[item].get_raw(), False)[2:]
                mnemonic = self.database[item].get_opcode() + ' ' +  self.database[item].get_ins_str()
                if address_list[item] in jump_addrs:
                    print(jump_addrs[address_list[item]])
                print (hex_str + "\t" + instruction + "\t\t\t" + mnemonic)