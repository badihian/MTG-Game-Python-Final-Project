import gameBoard
import playerLib
import buildDecks
import cardEffects
from urllib import request

board = gameBoard.Board()
player1 = playerLib.Player("Player1")
computer = playerLib.Player("Computer")

player1.initialDraw()
computer.initialDraw()

# def displayHand(player):
player1.showHand()
# player1.sortHand()
# player1.showHand()

board.drawImage(player1.showHand())
board.displayLife(player1)
board.displayLife(computer)

board.win.getMouse()
board.exit()