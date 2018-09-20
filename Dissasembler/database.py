import copy
import constants

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
    
    def __convert_address(self, address):
        address.reverse()
        hex_list = [hex(x) for x in address]
        hex_str = str(hex_list).replace(',','').replace('[','').replace(']','').replace(' ', '').replace('x','').replace('0','').replace("'",'')
        return '0x' + hex_str.zfill(len(address)*2)

    def __format_mod_rm_text(self, mod, rm, displacement):
        '''
        This routine formats the mod/rm byte
        '''
        register = constants.registers[rm]

        if displacement is not None:
            hex_disp = self.__convert_address(displacement)

        if mod is 3:
            return register
        if mod is 0:
            return '[' + register + ']'
        if mod is 2:
            return '[' + register + '+' + hex_disp + ']'

    def dissasemble_database(self):
        
        item = self.database[0]
        # Process 'regular' opcodes
        if item.get_kind() is constants.Ins_Kind.REGULAR:
            reg = str(constants.registers[item.get_reg_op()])
            item.set_ins_str(reg + ', ' + self.__format_mod_rm_text(item.get_mod(), item.get_rm(), None))
        # Process opcodes with displacement
        if item.get_kind() is constants.Ins_Kind.DISPLACEMENT:
            reg = str(constants.registers[item.get_reg_op()])
            item.set_ins_str(reg + ', ' + self.__format_mod_rm_text(item.get_mod(), item.get_rm(), item.get_disp()))
        # Process opcodes with embedded values
        if item.get_kind() is constants.Ins_Kind.EMBEDDED:
            reg = str(constants.registers[item.get_reg_op()])
            item.set_ins_str(reg)
        # Process opcodes with return values
        if item.get_kind() is constants.Ins_Kind.RETURN:
            item.set_ins_str(self.__convert_address(item.get_disp()))
        # Process opcodes with "large" values
        if item.get_kind() is constants.Ins_Kind.LARGE:
            reg = self.__format_mod_rm_text(item.get_mod(), item.get_rm(), item.get_disp())
            print(reg)
            item.set_ins_str(reg + ', ' + self.__convert_address(item.get_immediate()))
        # Process opcodes with "immediate" values
        if item.get_kind() is constants.Ins_Kind.IMMEDIATE:
            item.set_ins_str('eax, ' + self.__convert_address(item.get_immediate()))            
