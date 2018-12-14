import json

with open("AllCards.json", "r") as mtgJSON:
    mtgString = json.load(mtgJSON)

with open("scryfall-default-cards.json", "r") as scryfallJSON:
    scryString = json.load(scryfallJSON)

totalEqual = 0

totalMTG = 0
index = 0
for card in mtgString:
    # if index < 10:
    #     print(f"{mtgString[card]['name']}")
    #     index += 1
    for scry in scryString:
        name = scry['name']
        if mtgString[card]['name'] == name:
            totalEqual += 1
            break
        else:
            continue
    totalMTG +=1

print(f"totalMTG = {totalMTG}")
print("============================================")
totalScry = 0
index = 0
for card in scryString:
    if index < 10:
        print(f"{card['name']}")
        index += 1
    totalScry +=1

print(f"totalScry = {totalScry}")

print(f"totalEqual = {totalEqual}")