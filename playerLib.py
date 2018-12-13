import buildDecks

class Player:

    def __init__(self, name):
        self.name = name
        self.deck = buildDecks.whiteWeenie()
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

# player1 = Player("player1")
# print(player1.drawCard())
# while True:
#     x = input("Draw another? ")
#     if x == 'y':
#         print(player1.drawCard())
#     else:
#         break