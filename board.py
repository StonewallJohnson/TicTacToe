class Board:
    def __init__(self):
        self.boardCon = [" ", " ", " ",
                         " ", " ", " ",
                         " ", " ", " "]
        self.rows = self.__getRows()
        self.columns = self.__getColumns()
        self.diagonals = self.__getDiagonals()
        self.xTurn = True
        
    def printBoard(self):
        """Prints the board"""
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
          
    def makeMove(self, index):
        if (index >= 0 or index <= 8) and not self.spotTaken(index):
            if self.xTurn:
                self.boardCon[index] = 'X'
            else:
                self.boardCon[index] = "O"
            self.xTurn = not self.xTurn
        else:
            print("Can not make a move there!")

    def spotTaken(self, index):
        """Returns whether the index has already been picked"""
        if self.boardCon[index] == " ":
            return False
        else:
            return True 

    def __getRows(self):
        """Returns a list of the rows of the board"""
        rows = [self.boardCon[0:3], self.boardCon[3:6], self.boardCon[6:9]]
        return rows

    def __getColumns(self):
        """Returns a list of the columns of the board"""
        columns = [self.boardCon[0:7:3], self.boardCon[1:8:3], self.boardCon[2:9:3]]
        return columns

    def __getDiagonals(self):
        """Returns a list of the diagonals of the board"""
        diagonals = [self.boardCon[0:9:4], self.boardCon[6:0:-2]]
        return diagonals
    