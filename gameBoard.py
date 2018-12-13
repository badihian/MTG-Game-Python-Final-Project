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

background.draw(win)
deckImage.draw(win)
deckImageFlipped.draw(win)
handImage.draw(win)

win.getMouse()
win.close()