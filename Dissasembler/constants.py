from enum import Enum

'''
Constants
'''
opcodes =  {0x81: {0: 'mi', 1: {0: 'add', 6: 'xor', 3: 'sbb', 1: 'or', 7: 'cmp', 4: 'and'}},
            0xFF: {0: 'mi', 1: {2: 'call', 1: 'dec', 0: 'inc', 4: 'jmp', 6: 'push'}},
            0xF7: {0: 'mi', 1: {3: 'neg', 2: 'not', 4: 'mul', 0: 'test', 7: 'idiv', 5: 'imul'}},
            0xD1: {0: 'm1', 1: {4: 'sal', 5: 'shr', 7: 'sar'}},
#            0x0F: {0x84: {0: 'd', 1: 'jz'}, 0x85: {0: 'd', 1: 'jnz'}, 0xAF: {0: "rm", 1: 'imul'}, 0xAE{0: 'm', 1: 'clflush'}},
            0xEB: {0: 'd',  1: 'jmp'},
            0xE9: {0: 'd',  1: 'jmp'},
            0x74: {0: 'd',  1: 'jz'},
            0x75: {0: 'd',  1: 'jnz'},
            0x31: {0: 'mr', 1: 'xor'},
            0x33: {0: 'rm', 1: 'xor'},
            0x35: {0: 'i',  1: 'xor'},
            0x01: {0: 'mr', 1: 'add'}, 
            0x03: {0: 'rm', 1: 'add'},
            0x05: {0: 'i',  1: 'add'},
            0x21: {0: 'mr', 1: 'and'}, 
            0x23: {0: 'rm', 1: 'and'},
            0x25: {0: 'i',  1: 'and'},
            0x85: {0: 'mr', 1: 'test'}, 
            0xA9: {0: 'i',  1: 'test'},
            0x19: {0: 'mr', 1: 'sbb'}, 
            0x1B: {0: 'rm', 1: 'sbb'},
            0x1D: {0: 'i',  1: 'sbb'},                        
            0xE8: {0: 'm',  1: 'call'},     
            0x39: {0: 'mr', 1: 'cmp'}, 
            0x3B: {0: 'rm', 1: 'cmp'},
            0x3D: {0: 'i',  1: 'cmp'},    
            0x09: {0: 'mr', 1: 'or'}, 
            0x0B: {0: 'rm', 1: 'or'},
            0x0D: {0: 'i',  1: 'or'},
            0x8F: {0: 'm',  1: 'pop'},
            0x58: {0: 'o',  1: 'pop'},       
            0x50: {0: 'o',  1: 'push'},
            0x68: {0: 'i',  1: 'push'},    
            0x48: {0: 'o',  1: 'dec'},       
            0x40: {0: 'o',  1: 'inc'},                                   
            0xC7: {0: 'mi', 1: 'mov'},
            0x89: {0: 'mr', 1: 'mov'},
            0x8B: {0: 'rm', 1: 'mov'},
            0xB8: {0: 'oi', 1: 'mov'},
            0xA5: {0: 'zo', 1: 'movsd'},
            0xCB: {0: 'zo', 1: 'retf'},
            0xCA: {0: 'i',  1: 'retf'},
            0xC3: {0: 'zo', 1: 'retn'},
            0xC2: {0: 'i',  1: 'retn'},
            0xE7: {0: 'i',  1: 'out'},
            0x8D: {0: 'rm', 1: 'lea'},
            0x90: {0: 'zo', 1: 'nop'}}

registers = {0: 'eax', 1: 'ecx', 2: 'edx', 3: 'ebx', 4:'esp', 5:'ebp', 6: 'esi', 7: 'edi'}