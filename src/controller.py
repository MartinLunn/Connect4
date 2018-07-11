from model import Model
from view import View
import numpy as np
import constants

class Controller:
    def __init__(self):
        self.__model = Model()
        self.__view = View()

    def getView(self):
        return self.__view

    def getModel(self):
        return self.__model

def main():
    controller = Controller()
    controller.getView().printConsole(controller.getModel().getBoard().getBoard())
    #controller.getModel().getBoard().setBoardValue(0,0,1)
    i = 0
    for j in range(constants.boardHeight):
        for k in range(constants.boardWidth):
            controller.getModel().getBoard().setBoardValue(j,k,i)
            i += 1

    for j in range(constants.boardWidth):
        for k in range(0, j):
            controller.getModel().getBoard().setBoardValue(k,j,0)

    controller.getView().printConsole(controller.getModel().getBoard().getBoard())

    controller.getModel().makeMove(6, 1)
    controller.getModel().makeMove(6, 22)
    controller.getModel().makeMove(0, 21)
    #controller.getModel().makeMove(0, 22)  #expected failure

    controller.getView().printConsole(controller.getModel().getBoard().getBoard())

    print(controller.getModel().getBoard().areNConnected())
    input()

main()
