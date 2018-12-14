import buildDecks
import tkinter
import PIL
import graphics
from urllib import request
import io

class Player:

    def __init__(self, name):
        self.name = name
        self.deck = buildDecks.whiteWeenie()
        self.hand = []
        self.life = 20
    
    def showName(self):
        return self.name
    
    def showLife(self):
        return self.life
    
    def addLife(self, amount):
        self.life += amount
    
    def subtractLife(self, amount):
        self.life -= amount
    
    def drawCard(self):
        return self.deck.popCard()
    
    def initialDraw(self):
        for _ in range(7):
            self.addHand(self.drawCard())
    
    def addHand(self, card):
        self.hand.append(card)
    def getHand(self):
        return self.hand
    def showHand(self):
        images = []
        if self.name == "Computer":
            y = 150
        else:
            y = 650
        x = (1322/2) - ((len(self.hand)-1)*50)
        print(f"X EQUALS = {x}")
        for card in self.hand:
            print(card)
            images.append(card.displayCard(x, y))
            print(type(card.displayCard(x, y)))
            x += 100
            # imageURL = card.showImageURL()
            # print(imageURL)
            # raw_data = request.urlopen(imageURL).read()
            # image = PIL.Image.open(io.BytesIO(raw_data))
            # image = image.resize((97, 142), PIL.Image.ANTIALIAS)
            # image = graphics.Image(graphics.Point(x, 250), image)
            # x += 142
        return images

    def getHandTypes(self):
        types = []
        for card in self.hand:
            types.append(card.showTypes())
        return types
    def getType(self, card):
        return card.types
    def sortHand(self):
        self.hand = self.hand.sort(key=self.getType)

# player1 = Player("player1")
# print(player1.drawCard())
# while True:
#     x = input("Draw another? ")
#     if x == 'y':
#         print(player1.drawCard())
#     else:
#         break