import buildDecks
import json
import playerLib
from graphics import *
from urllib import request

class Board:
    def __init__(self):
        self.background = Image(Point(1322/2,797/2), "Images/background-image.png")
        backgroundWidth = self.background.getWidth()
        backgroundHeight = self.background.getHeight()

        self.win = GraphWin("Magic the Gathering", backgroundWidth, backgroundHeight)
        self.win.setBackground(color_rgb(104, 0, 196))

        deckImage = Image(Point(1200, 650), "Images/Magic_card_back.png")
        deckImageFlipped = Image(Point(122, 147), "Images/Magic_card_back_flipped.png")
        self.handBackground = Image(Point(1322/2, 797 - 125), "Images/hand-background2.png")

        playerDice = Image(Point(122, 650), "Images/20-sided-die1.png")
        computerDice = Image(Point(1200, 147), "Images/20-sided-die2.png")

        # cardImage = Image(Point(1322/2, 797/2), "https://img.scryfall.com/cards/normal/front/6/6/663029eb-8002-42fd-b1ad-02f249bc0ffd.jpg?1542672088")


        print(f"type(background) in gameBoard = {type(self.background)}")
        self.background.draw(self.win)
        deckImage.draw(self.win)
        deckImageFlipped.draw(self.win)
        self.handBackground.draw(self.win)
        playerDice.draw(self.win)
        computerDice.draw(self.win)
        # cardImage.draw(win)
    
    def drawImage(self, images):
        for image in images:
            print(f"type(image) in gameBoard = {type(image)}")
            image.draw(self.win)
    
    def displayLife(self, player):
        if player.showName() == "Computer":
            x = 1200
            y = 152
        else:
            x = 122
            y = 655
        message = Text(Point(x, y), player.showLife())
        message.draw(self.win)

    def exit(self):
        self.win.close()

        # win.getMouse()
        # win.close()