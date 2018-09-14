class Database:
    def __init__(self):
        '''
        Initialization
        '''
        self.database = []

    def insert(self, byte):
        '''
        Inserts a byte to the instruction database
        '''
        self.database.append(byte)
