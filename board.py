class Board:
    rules = """Welcome to TicTacToe!
Choose who you want to go first and they will be Xs
To make a move, enter a number ranging from 1-9
Each number corresponds to the square shown below
   |   |
 1 | 2 | 3
-----------
 4 | 5 | 6
-----------
 7 | 8 | 9
   |   |   """
    def __init__(self):
        self.boardCon = [" ", " ", " ",
                         " ", " ", " ",
                         " ", " ", " "]
        self.rows = self.__getRows()
        self.columns = self.__getColumns()
        self.diagonals = self.__getDiagonals()
        self.xTurn = True
        self.turnsTaken = 0
        self.status = ""
        
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
          
    def makeMove(self):
        """Makes the move if it is legal and updates the board"""
        index = self.getMove()
        if (index >= 0 or index <= 8) and not self.spotTaken(index):
            if self.xTurn:
                self.boardCon[index] = 'X'
            else:
                self.boardCon[index] = "O"
            
            self.xTurn = not self.xTurn
            self.rows = self.__getRows()
            self.columns = self.__getColumns()
            self.diagonals = self.__getDiagonals()
            self.turnsTaken += 1
            return True
        else:
            print("Can not make a move there!")
            return False

    def hasWinner(self):
        """Returns whether or not there is a winning
            position on the board
        """
        for row in self.rows:
            #check for row win
            if row[0] == row[1] and row[0] == row[2]:
                if row[0] != " ":
                    self.status = "winner"
                    return True
        
        for column in self.columns:
            #check for column win
            if column[0] == column[1] and column[0] == column[2]:
                if column[0] != " ":
                    self.status = "winner"
                    return True
        
        for diagonal in self.diagonals:
            #check for diagonal win
            if diagonal[0] == diagonal[1] and diagonal[0] == diagonal[2]:
                if diagonal[0] != " ":
                    self.status = "winner"
                    return True
        
        if self.turnsTaken == 9:
            self.status = "tie"
            return True
        return False 

    def getMove(self):
        """Gets the user input for the move"""
        move = int(input("Make a move: ")) - 1
        return move
    
    def spotTaken(self, index):
        """Returns whether the index has already been picked"""
        if self.boardCon[index] == " ":
            return False
        else:
            return True 

    def showEnd(self):
        if self.status == "winner":
            if self.xTurn:
                print("*****  Os win!!! *****")
            else:
                print("*****  Xs win!!!  *****")
        else:
            print("*****  It's a draw!!!  *****")

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

def main():
    print(Board.rules)
    inp = input("Do you want to play TicTacToe?[Y/N]")
    
    while inp == 'Y' or inp == "y":
        #until no longer wants to play
        board = Board()
        board.printBoard()
        while not board.hasWinner():
            #until a winning move is found
            validMove = board.makeMove()
            while not validMove:
                #until valid move made
                validMove = board.makeMove()
            board.printBoard()
        board.showEnd()
        inp = input("Do you want to again?[Y/N]")


if __name__ == "__main__":
    main()    