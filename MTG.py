import json
import random

class Card:

    def __init__(self, name, types):
        self.name = name
        self.types = None
        self.cmc = None
        self.manaCost = None
        self.colors = None
        self.colorIdentity = None
        self.text = None
        self.imageURL = None

    def showName(self):
        return self.name

    def getTypes(self):
        self.types = jsonString[self.name]['types']
    def showTypes(self):
        return self.types

    def getCMC(self):
        self.cmc = jsonString[self.name]['cmc']
    def showCMC(self):
        return self.cmc

    def getManaCost(self):
        self.manaCost = jsonString[self.name]['manaCost']
    def showManaCost(self):
        return self.manaCost
    
    def getColors(self):
        self.colors = jsonString[self.name]['colors']
    def showColors(self):
        return self.colors
    
    def getColorIdentity(self):
        self.colorIdentity = jsonString[self.name]['colorIdentity']
    def showColorIdentity(self):
        return self.colorIdentity

    def getText(self):
        self.text = jsonString[self.name]['text']
    def showText(self):
        return self.text
    
    def getImageURL(self):
        self.imageURL = jsonString[self.name]['imageName']
    def showImageURL(self):
        return self.imageURL
    
    def getCard(self):
        self.getTypes()
        self.getCMC()
        if 'manaCost' in jsonString[self.name]:
            self.getManaCost()
        if 'text' in jsonString[self.name]:
            self.getText()
        if 'colorIdentity' in jsonString[self.name]:
            self.getColorIdentity()
        if 'colors' in jsonString[self.name]:
            self.getColors()



class Deck:
    def __init__(self, colorChoice, landCount, creatureCount, creatureDict, artifactCount, enchantmentCount, planeswalkerCount):
        self.colorChoice = colorChoice
        self.landCount = landCount
        self.creatureCount = creatureCount
        self.creatureDict = creatureDict
        self.artifactCount = artifactCount
        self.enchantmentCount = enchantmentCount
        self.planeswalkerCount = planeswalkerCount

    def findOfColor(self, cardType):
        allNames = []
        index = 0
        for color in self.colorChoice:
            for name in jsonString:
                if 'colors' not in jsonString[name]:
                    continue
                if color in jsonString[name]['colors'] and set(jsonString[name]['colors']).issubset(self.colorChoice) and cardType in jsonString[name]['types']:
                    allNames.append(jsonString[name]['name'])
                    index += 1
        return allNames

    def getCreatures(self):
        allNames = self.findOfColor("Creature")
        self.creatureNames = []
        index = 0
        for i in range(len(colorChoice)):
            for key in self.creatureDict[i].keys():
                if self.creatureDict[i][key] > 0:
                    for value in range(self.creatureDict[i][key]):
                        random.shuffle(allNames)
                        while True:
                            for name in allNames:
                                if int(jsonString[name]['cmc']) == int(key):
                                    self.creatureNames.append(Card(name, "Creature"))
                                    index += 1
                                    break
                                else:
                                    continue 
                            break

    def showCreatures(self):
        for card in self.creatureNames:
            card.getCMC()
            card.getColors()
            card.getManaCost()
            print(f"Name: {card.showName()}, Type: {card.showTypes()}, CMC: {card.showCMC()}, Colors: {card.showColors()}")

with open("AllCards.json", "r") as mtgJSON:
    jsonString = json.load(mtgJSON)

mtgDict = {0 : ""}

i = 0
for card in jsonString:
    mtgDict[i] = jsonString[card]['name']
    i += 1

i=0
mtgList = [0] * len(jsonString)
for key, value in mtgDict.items():
    mtgList[i] = key
    i += 1

random.shuffle(mtgList)

colorCount = int(input("How many colors would you like to play: "))

colorChoice = [""] * colorCount
landCount = [0] * colorCount
creatureCount = [0] * colorCount
creatureDict = [{1 : 0, 2 : 0, 3 : 0, 4 : 0, 5 : 0, 6 : 0, 7 : 0, 8 : 0, 9 : 0, 10 : 0, 11 : 0, 12 : 0, 13 : 0, 14 : 0, 15 : 0, 16 : 0}] * colorCount

for i in range(colorCount):
    colorChoice[i] = input("Enter one of the colors (white/blue/black/green/red): ")
    landCount[i] = int(input("Enter the number of lands you want of this color: "))
    creatureCount[i] = int(input("Enter the number of creatures you want of this color: "))
    count = creatureCount[i]
    print("Now choose what the mana cost of each of those creatures should be.")
    while count > 0:
        manaCost = int(input("Enter the mana cost: "))
        manaCount = int(input("Enter the number of creature you want with this mana cost: "))

        creatureDict[i][manaCost] = manaCount
        count -= manaCount

artifactCount = int(input("Enter the number of artifacts you want: "))
enchantmentCount = int(input("Enter the number of enchantments you want: "))
planeswalkerCount = int(input("Enter the number of planes walkers you want: "))

deck1 = Deck(colorChoice, landCount, creatureCount, creatureDict, artifactCount, enchantmentCount, planeswalkerCount)

deck1.getCreatures()
deck1.showCreatures()