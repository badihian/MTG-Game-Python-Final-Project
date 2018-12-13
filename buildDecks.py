import json
from urllib import request
from random import shuffle

with open("JSON/AllCards.json", "r") as mtgJSON:
    mtgString = json.load(mtgJSON)

with open("JSON/scryfall-default-cards.json", "r") as scryfallJSON:
    scryString = json.load(scryfallJSON)

class Token:

    def __init__(self, name, cardType, colorIdentity, power, toughness, text, effect=None):
        self.name = name
        self.types = [cardType]
        self.power = power
        self.toughness = toughness
        self.text = text
        self.colorIdentity = colorIdentity
        # self.imageURL = None
        self.effect = []
        if effect != None:
            self.effect.append(effect)

    def showName(self):
        return self.name
    
    def showTypes(self):
        return self.types
    
    def showPower(self):
        return self.power
    
    def showToughness(self):
        return self.toughness
    
    def showText(self):
        return self.text

    def showEffect(self):
        return self.effect
    def addEffect(self, effect):
        self.effect.append(effect)
    
    def addStats(self, power=0, toughness=0):
        print(f"Power before: {self.showPower()}")
        print(f"Toughness before: {self.showToughness()}")
        self.power += power
        self.toughness += toughness
        print(f"Power after: {self.showPower()}")
        print(f"Toughness after: {self.showToughness()}")


class Card:

    def __init__(self, name):
        self.name = name
        self.types = []
        self.cmc = None
        self.manaCost = None
        self.colors = []
        self.colorIdentity = []
        self.power = None
        self.toughness = None
        self.text = None
        self.imageURL = None
        self.effect = []
        self.loreCounter = 0
        self.getCard()

    def showName(self):
        return self.name

    def getTypes(self):
        for cardType in mtgString[self.name]['types']:
            self.types.append(cardType)
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
        for color in mtgString[self.name]['colors']:
            self.colors.append(color)
    def showColors(self):
        if self.colors != None:
            return self.colors
        else:
            return "No Colors"
    
    def getColorIdentity(self):
        if "colorIdentity" in mtgString[self.name]:
            for colorID in mtgString[self.name]['colorIdentity']:
                self.colorIdentity.append(colorID)
    def showColorIdentity(self):
        if self.colorIdentity != None:
            return self.colorIdentity
        else:
            return "No Color Identity"
    
    def getPower(self):
        if "power" in mtgString[self.name]:
            self.power = int(mtgString[self.name]['power'])
        else:
            self.power = "No Power"
    def showPower(self):
        return self.power
    
    def getToughness(self):
        if "toughness" in mtgString[self.name]:
            self.toughness = int(mtgString[self.name]['toughness'])
        else:
            self.toughness = "No Toughness"
    def showToughness(self):
        return self.toughness

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

    def addEffect(self, effect):
        self.effect.append(effect)
    def showEffect(self):
        return self.effect
    
    def addStats(self, power=0, toughness=0):
        print(f"Power before: {self.showPower()}")
        print(f"Toughness before: {self.showToughness()}")
        self.power += power
        self.toughness += toughness
        print(f"Power after: {self.showPower()}")
        print(f"Toughness after: {self.showToughness()}")
    
    def getCard(self):
        self.getTypes()
        self.getCMC()
        self.getImageURL()
        self.getPower()
        self.getToughness()
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
        print(f"Power: {self.showPower()}")
        print(f"Toughness: {self.showToughness()}")
        print(f"Text: {self.showText()}")
        print(f"Color Identity: {self.showColorIdentity()}")
        print(f"Colors: {self.showColors()}")
        print("\n")
    
    def __str__(self):
        return self.name
        

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

    def popCard(self):
        return self.cards.pop()

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

# testDeck = whiteWeenie()
# # testDeck.printCardNames()
# print("\n================================")
# testDeck.printDeck()
# print("\n================================\n")
# cardSet = sorted(set(testDeck.cardNames))
# print(f"There are {len(testDeck.cardNames)} cards in your deck:")
# for name in cardSet:
#     print(f"{testDeck.cardNames.count(name):0>2} of '{name}'")