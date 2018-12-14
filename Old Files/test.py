import json

with open("AllCards.json", "r") as mtgJSON:
    jsonString = json.load(mtgJSON)

class Card:

    def __init__(self, name, types):
        self.name = name
        self.types = types
        self.cmc = None
        self.manaCost = None
        self.colors = None
        self.text = None
        self.imageName = None


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

    def getText(self):
        self.text = jsonString[self.name]['text']
    def showText(self):
        return self.text
    
    def getImageName(self):
        self.imageName = jsonString[self.name]['imageName']
    def showImageName(self):
        return self.imageName

def shuffleCreatures(colorChoice):
        allNames = []
        index = 0
        for color in colorChoice:
            for name in jsonString:
                if 'colors' not in jsonString[name]:
                    continue
                if color in jsonString[name]['colors'] and set(jsonString[name]['colors']).issubset(colorChoice):
                    allNames.append(jsonString[name]['name'])
                    print(f"Name: {allNames[index]}, color: {jsonString[name]['colors']}")
                    index += 1


card = Card("Adorable Kitten", ["Creature"])
card.getCMC()
print(card.showCMC())
card.getManaCost()
print(card.showManaCost())
card.getColors()
print(card.showColors())
card.getText()
print(card.showText())
card.getImageName()
print(card.showImageName())

colorChoice = ["Red", "Blue"]
print(colorChoice[0])
shuffleCreatures(colorChoice)

myDict = {1:"hi", 2:"bye", 3:"welcome"}
for key in myDict.keys():
    print(key)