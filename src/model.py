import math
import numpy as np
import constants

class Model:
    #p1 and p2 are booleans indiciating whether they're human players
    def __init__(self, p1 = True, p2 = True, boardHeight = constants.boardHeight, boardWidth = constants.boardWidth):
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
        horizontal = self.checkHorizontal()
        if (horizontal is not None):
            return horizontal

        vertical = self.checkVertical()
        print(str(vertical))
        if (vertical is not None):
            return vertical

        diagonal = self.checkDiagonal()
        if (diagonal is not None):
            return diagonal

    def checkHorizontal(self):
        lastStartIdx = constants.boardWidth - constants.connectNumber
        lastEndIdx = constants.boardWidth
        startIdx = 0
        endIdx = 1
        currLength = 0
        for i in range(constants.boardHeight):
            while(startIdx <= lastStartIdx and endIdx <= lastEndIdx):
                currLength = endIdx - startIdx
                if (currLength >= constants.connectNumber):
                    return self.getBoard()[i, endIdx - 1]       #player number
                if (self.getBoard()[i, endIdx] == self.getBoard()[i, endIdx - 1]):
                    endIdx += 1
                else:
                    startIdx += 1
                    endIdx = startIdx + 1
        return None

    def checkVertical(self): #not working? TODO
        lastStartIdx = constants.boardHeight - constants.connectNumber
        lastEndIdx = constants.boardHeight
        startIdx = 0
        endIdx = 1
        currLength = 0
        for i in range(constants.boardWidth):
            while(startIdx <= lastStartIdx and endIdx <= lastEndIdx):
                currLength = endIdx - startIdx
                print("i: " + str(i))
                print("startIdx " + str(startIdx))
                print("endIdx " + str(endIdx))
                print("currLength " + str(currLength))
                if (currLength >= constants.connectNumber):
                    return self.getBoard()[endIdx - 1, i]       #player number
                if (self.getBoard()[endIdx, i] == self.getBoard()[endIdx - 1, i]):
                    endIdx += 1
                else:
                    startIdx += 1
                    endIdx = startIdx + 1
        return None

    def checkDiagonal(self):
        return None


class Player:
    def __init__(self, trueIfHuman = True):
        if (trueIfHuman):
            print("this player is human")
        else:
            print("this player is not human")
