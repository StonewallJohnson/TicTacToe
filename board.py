class Board:
    def __init__(self):
        self.boardContainer = [[" ", "|", " ", "|", " "],
                               [" ", "|", " ", "|", " "],
                               [" ", "|", " ", "|", " "]]
        
    def printBoard(self):
        for row in self.boardContainer:
            for val in row:
                print(val, end="")
            print("\n______")
        print()