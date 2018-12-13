import buildDecks
import json
from graphics import *

background = Image(Point(1322/2,797/2), "Images/background-image.png")
backgroundWidth = background.getWidth()
backgroundHeight = background.getHeight()

win = GraphWin("Magic the Gathering", backgroundWidth, backgroundHeight)
win.setBackground(color_rgb(104, 0, 196))

deckImage = Image(Point(1200, 650), "Images/Magic_card_back.png")
deckImageFlipped = Image(Point(122, 147), "Images/Magic_card_back_flipped.png")
handImage = Image(Point(1322/2, 688), "Images/hand-background2.png")

cardImage = Image(Point(1322/2, 797/2), "https://img.scryfall.com/cards/normal/front/6/6/663029eb-8002-42fd-b1ad-02f249bc0ffd.jpg?1542672088")

background.draw(win)
deckImage.draw(win)
deckImageFlipped.draw(win)
handImage.draw(win)
cardImage.draw(win)

win.getMouse()
win.close()