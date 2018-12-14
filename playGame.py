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

board.displayLife(player1)
board.displayLife(computer)
board.drawImage(player1.showHand())

board.win.getMouse()
board.exit()