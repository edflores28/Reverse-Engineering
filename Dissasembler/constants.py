from enum import Enum

'''
Constants
'''
opcodes = {0x31: 'xor', 0x01: 'add', 0x89: 'mov', 0xB8: 'mov'}

large_opcodes = {0x81: {0: 'add', 6: 'xor', 3: 'sbb', 1: 'or', 7: 'cmp', 4: 'and'}}

disp_opcodes = {0x8B: 'mov'}

embed_opcodes = {0x50: 'push', 0x58: 'pop'}

ret_opcodes = {0xC2: 'ret'}

immed_opcode = {0x05: 'add', 0x25: 'and', 0x3D: 'cmp', 0x35: 'xor', 0xA9: 'test', 0x1D: 'sbb', 0x0D: 'or'}

registers = {0: 'eax', 1: 'ecx', 2: 'edx', 3: 'ebx', 4:'esp', 5:'ebp', 6: 'esi', 7: 'edi'}

'''
Enumeration
'''
class Ins_Kind(Enum):
    REGULAR = 1
    LARGE = 2
    DISPLACEMENT =3
    EMBEDDED = 4
    RETURN = 5
    IMMEDIATE = 6