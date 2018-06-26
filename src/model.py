import math
import numpy as np
import constants

class Model:
    def __init__(self, p1 = True, p2 = True, boardHeight = constants.boardHeight, boardWidth = constants.boardWidth): #p1 and p2 are booleans indiciating whether they're human players
        if (p1):
            self.__p1 = Player(p1)

        if (p2):
            self.__p2 = Player(p2)

        self.__board = Board(boardHeight, boardWidth)

    def getBoard(self):
        return self.__board;

    def checkColFull(self, col):    #col is int
        try:
            col = int(col)
        except:
            ValueError("Col (%d) cannot be coerced to int" % col)

        if (col >= constants.boardWidth):
            raise ValueError("Col (%d) is not within bounds" % col)

        boardCol = self.__board.getBoard()[:, col]
        if (boardCol.min == 0):
            return True
        return False

    def findLowestEmptyIndex(self, col):
        try:
            col = int(col)
        except:
            ValueError("Col (%d) cannot be coerced to int" % col)

        if (col >= constants.boardWidth):
            raise ValueError("Col (%d) is not within bounds" % col)

        boardCol = self.__board.getBoard()[:, col]
        i = boardCol.shape[0] - 1       #boardCol's 1st dimension's length. - 1 because we start indexing at 0
        for element in reversed(boardCol):
            if (element == 0):
                return i
            i -=1

        raise ValueError("No empty indices in findLowestEmptyIndex with params col: %d and board \n%s" % (col, self.__board.getBoard()))

    def makeMove(self, col, player):
        try:
            col = int(col)
        except:
            ValueError("Col (%d) cannot be coerced to int" % col)

        try:
            player = int(player)
        except:
            ValueError("player (%d) cannot be coerced to int" % player)

        #if (player != 1 or player != 2):         TODO uncomment
        #    raise ValueError("Player (%d) is not a valid player" % player)

        if (not self.checkColFull(col)): #if col has room
            bottommostEmptyRow = self.findLowestEmptyIndex(col)
            self.__board.setBoardValue(bottommostEmptyRow, col, player)
        else:
            raise ValueError("TEMP ERROR DO SOMETHING ELSE")

    def areNConnected(self):            #returns 0 for no winner or player number
        return self.__board.areNConnected()

class Board:
    def __init__(self, boardHeight = constants.boardHeight, boardWidth = constants.boardWidth):
        #board = [[0 for x in range(boardWidth)] for y in range(boardHeight)]
        self.__board = np.zeros((boardHeight, boardWidth), dtype=int)

    def getBoard(self):
        return self.__board

    def setBoardValue(self, row, col, value):
        #if (value not in constants.validBoardValues):      TODO uncomment
            #raise ValueError("Value (%d) is not a valid value" % value)
        try:
            value = int(value)
        except ValueError:
            print("Value (%d) is not coercible to int from inside setBoardValue" % value)
        temp = self.__board[row, col]
        self.__board[row, col] = value
        return temp

    def areNConnected(self):            #returns 0 for no winner, or player number
        for i in range(constants.boardWidth):
            for j in range(constants.boardHeight):
                winner = self.isThisIndexPartOfNConnected(i,j)
                if (winner != 0):
                    return winner

    def isThisIndexPartOfNConnected(self, i, j):
        if (i <= constants.boardHeight - constants.connectNumber):
            #check down
        if (j <= constants.boardWidth - constants.connectNumber):
            #check right
        #


class Player:
    def __init__(self, trueIfHuman = True):
        if (trueIfHuman):
            print("this player is human")
        else:
            print("this player is not human")
