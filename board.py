class Board:
    def __init__(self):
        self.boardCon = ["a", "b", "c",
                         "d", "e", "f",
                         "g", "h", "i"]
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
        rows = [self.boardCon[0:3], self.boardCon[3:6], self.boardCon[6:9]]
        return rows

    def __getColumns(self):
        columns = [self.boardCon[0:7:3], self.boardCon[1:8:3], self.boardCon[2:9:3]]
        return columns

    def __getDiagonals(self):
        diagonals = [self.boardCon[0:9:4], self.boardCon[6:0:-2]]
        return diagonals