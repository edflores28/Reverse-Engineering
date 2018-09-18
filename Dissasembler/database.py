import copy

class Database:
    def __init__(self):
        '''
        Initialization
        '''
        self.database = []
        self.counts = []
        self.total_bytes = -1
        self.formatted = []

    def insert(self, byte):
        '''
        Inserts a byte to the database
        '''
        self.database.append(copy.deepcopy(byte))

    def format(self):
        print(self.database)