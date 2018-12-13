import json
import graphics
import buildDecks

def cardEffect(card):
    if card.showName() == "Dauntless Bodyguard":
        dauntlessBodyguard(card)

def dauntlessBodyguard(card):
    print("Choose a creature,\nit will be indestructible until end of turn.")

def flyingCreature(card):
    card.addEffect("Flying")

def ascend(player):
    # player.addEffect("City's Blessing")
    return

def sunbhornSentry(card):
    card.addStats(3)

def skymarcherAspirant(card):
    if "Flying" not in card.showEffect():
        flyingCreature(card)

def convoke(player, card):
    print("Tap creatures for mana.\nEach creature supplies one color of its color.")
    whiteCount = 0
    redCount = 0
    blueCount = 0
    greenCount = 0
    blackCount = 0
    convokedCards = []
    # tap cards and untap cards
    # convokedCards.append(tappedCard)
    # convokedCards.remove(untappedCard)
    # add one mana for each card tapped
    # update display of mana count for each tap and untap
    # click done or cancel
    # 
    # if clicked done:
    #     player.addMana(whiteCount, redCount, blueCount, greenCount, blackCount)
    #     if card.showName() == "Venerated Loxodon":
    #          veneratedLoxodon(convokedCards)

def conclaveTribunal():
    print("Choose a nonland permanent your opponent controls and exile it.")
    # click on card
    # card.addEffect("Exiled by Conclave")
    # board.exile(card)

def historyOfBenalia(card, player, board):
    card.loreCounter += 1
    if card.loreCounter == 1 or card.loreCounter == 2:
        knightToken = buildDecks.Token("Benalian Knight", "Token Creature", 
        'W', 2, 2, "This token was created by History of Benalia.")
        player.addCard(knightToken)
        board.addCard(knightToken, player)
        card.loreCounter += 1
    elif card.loreCounter == 3:
        for activeCard in board.activeCards:
            if activeCard.showName() == knightToken.showName() and activeCard.showPlayer() == player.showName():
                activeCard.addStats(2, 1)
        card.loreCounter += 1
    else:
        board.removeCard(card)
        player.removeCard(card)

def ajaniAdversary(board):
    print("Choose two creatures to gain +1/+1 counters.")
    # click on two cards
    # do the following after each click
    for card in board.activeCards:
        if card.showName() == chosenCard.showName() and "+1/+1 Counter" not in card.showEffect():
            card.addEffect("+1/+1 Counter")
            card.addStats(1, 1)
            break
        else:
            print("ERROR: Could not add +1/+1 counters.")
    # place +1/+1 chip image on card

def veneratedLoxodon(convokedCards):
    for convokedCard in convokedCards:
        for activeCard in board.activeCards:
            if card.showName() == chosenCard.showName() and "+1/+1 Counter" not in card.showEffect():
                card.addEffect("+1/+1 Counter")
                card.addStats(1, 1)
                break
            else:
                print("ERROR: Could not add +1/+1 counters.")

def legionsLanding(board, player):
    vampire = buildDecks.Token("Vampire Token", "Token Creature", 'W', 1, 1, "This token was created by Legion's Landing.", "Lifelink")
    board.addCard(vampire, player)

def lifelink(damage, player):
    player.addLife(damage)

def adantoVanguardPower(card):
    card.addStats(4)

def adantoVanguardIndest(card, player):
    card.addEffect("Indestructible")
    player.subtractLife(4)

def benalishMarshal(board, player):
    for card in board.activeCards:
        if card.showPlayer() == player.showName():
            card.addStats(1, 1)

testDeck = buildDecks.whiteWeenie()
# for card in testDeck.cards:
#     if card.showName() == "Snubhorn Sentry":
#         ascend(card)
#         break