import json
from urllib import request
from random import shuffle

with open("JSON/AllCards.json", "r") as mtgJSON:
    mtgString = json.load(mtgJSON)

with open("JSON/scryfall-default-cards.json", "r") as scryfallJSON:
    scryString = json.load(scryfallJSON)

class Card:

    def __init__(self, name):
        self.name = name
        self.types = None
        self.cmc = None
        self.manaCost = None
        self.colors = None
        self.colorIdentity = None
        self.text = None
        self.imageURL = None
        self.getCard()

    def showName(self):
        return self.name

    def getTypes(self):
        self.types = mtgString[self.name]['types']
    def showTypes(self):
        return self.types

    def getCMC(self):
        self.cmc = mtgString[self.name]['cmc']
    def showCMC(self):
        return self.cmc

    def getManaCost(self):
        self.manaCost = mtgString[self.name]['manaCost']
    def showManaCost(self):
        if self.manaCost != None:
            return self.manaCost
        else:
            return "No Mana Cost"
    
    def getColors(self):
        self.colors = mtgString[self.name]['colors']
    def showColors(self):
        if self.colors != None:
            return self.colors
        else:
            return "No Colors"
    
    def getColorIdentity(self):
        self.colorIdentity = mtgString[self.name]['colorIdentity']
    def showColorIdentity(self):
        if self.colorIdentity != None:
            return self.colorIdentity
        else:
            return "No Color Identity"

    def getText(self):
        self.text = mtgString[self.name]['text']
    def showText(self):
        if self.text != None:
            return self.text
        else:
            return "No Text"
    
    def getImageURL(self):
        found = False
        for card in scryString:
            if card['name'] in self.name and "image_uris" in card and "normal" in card["image_uris"]:
                self.imageURL = card['image_uris']['normal']
                found = True
                break
        if found == False:
            self.imageURL = "https://img.scryfall.com/cards/normal/front/6/6/663029eb-8002-42fd-b1ad-02f249bc0ffd.jpg?1542672088"
        # self.imageURL = mtgString[self.name]['imageName']
    def showImageURL(self):
        return self.imageURL
    
    def getCard(self):
        self.getTypes()
        self.getCMC()
        self.getImageURL()
        if 'manaCost' in mtgString[self.name]:
            self.getManaCost()
        if 'text' in mtgString[self.name]:
            self.getText()
        if 'colorIdentity' in mtgString[self.name]:
            self.getColorIdentity()
        if 'colors' in mtgString[self.name]:
            self.getColors()
    
    def showCard(self):
        print(self.showName())
        print(f"Types: {self.showTypes()}")
        print(f"CMC: {self.showCMC()}")
        print(f"Image URL: {self.showImageURL()}")
        print(f"Mana Cost: {self.showManaCost()}")
        print(f"Text: {self.showText()}")
        print(f"Color Identity: {self.showColorIdentity()}")
        print(f"Colors: {self.showColors()}")
        print("\n")
        

class whiteWeenie:
    def __init__(self):
        self.cardNames = []
        self.cards = []
        for i in range(4):
            self.cardNames.append("Adanto Vanguard")
            self.cardNames.append("Benalish Marshal")
            self.cardNames.append("Skymarcher Aspirant")
            self.cardNames.append("Snubhorn Sentry")
            self.cardNames.append("Venerated Loxodon")
            self.cardNames.append("History of Benalia")
            self.cardNames.append("Legion's Landing")
            if i > 0:
                self.cardNames.append("Dauntless Bodyguard")
                self.cardNames.append("Silverbeak Griffin")
            if i > 1:
                self.cardNames.append("Conclave Tribunal")
                self.cardNames.append("Ajani, Adversary of Tyrants")
        
        for j in range(22):
            self.cardNames.append("Plains")
        
        self.cardNames.sort()

        for name in self.cardNames:
            self.cards.append(Card(name))
            shuffle(self.cards)

    def printCardNames(self):
        for card in self.cardNames:
            print(f"{card}")
    
    def printDeck(self):
        i = 0
        for card in self.cards:
            card.showCard()

    
    # def __str__(self):
    #     for card in self.cardNames:
    #         print(card)

testDeck = whiteWeenie()
# testDeck.printCardNames()
print("\n================================")
testDeck.printDeck()
print("\n================================\n")
cardSet = sorted(set(testDeck.cardNames))
print(f"There are {len(testDeck.cardNames)} cards in your deck:")
for name in cardSet:
    print(f"{testDeck.cardNames.count(name):0>2} of '{name}'")