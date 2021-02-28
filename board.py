class Board:
    def __init__(self):
        self.boardCon = [" ", " ", " ",
                         " ", " ", " ",
                         " ", " ", " "]
        self.rows = self.__getRows()
        self.columns = self.__getColumns()
        self.diagonals = self.__getDiagonals()
        
    def printBoard(self):
        print("   |   |")
        print(" " + self.boardCon[0] + " | " + self.boardCon[1] + " | " + self.boardCon[2])
        print("   |   |")
        print("-----------")
        print("   |   |")
        print(" " + self.boardCon[3] + " | " + self.boardCon[4] + " | " + self.boardCon[5])
        print("   |   |")
        print("-----------")
        print("   |   |")
        print(" " + self.boardCon[6] + " | " + self.boardCon[7] + " | " + self.boardCon[8])
        print("   |   |")

    
    
    def __getRows(self):
        pass

    def __getColumns(self):
        pass

    def __getDiagonals(self):
        pass