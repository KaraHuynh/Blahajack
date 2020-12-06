import sys, pygame, random, card, deck, turn
import pygame.freetype

#init pygame
pygame.init()

size = width, height = 1920, 1080
screen = pygame.display.set_mode(size)
black = 0, 0, 0
white = 255, 255, 255
GAME_FONT = pygame.freetype.Font("./images/comicsans.ttf", 36)
cardCountLocations = [(604, 634), (935, 634), (1310, 634), (1668, 634), (607, 1039), (945, 1039), (1337, 1039), (1698, 1039)]
tableCardCountLocations = [[(544, 873),(1000, 888),(1459, 886)],[(547, 498),(1003, 496),(1458, 499)]]
p1_tablecounts = [0] * 3
p2_tablecounts = [0] * 3
currentScreen = 'Title'

#init game stuff
turn = turn.Turn(random.randint(1, 2))
moves = 3

player1Score = 0
player1Money = [0, 0, 0]
player2Score = 0
player2Money = [0, 0, 0]

deck = deck.Deck()
deck.reset()
deck.shuffle()
player1Hand = []
player2Hand = []
player1Matches = []
player2Matches = []

player1Counts = [0] * 8
player2Counts = [0] * 8

player1Win = False
player2Win = False

#functions
def startGame():
    global currentScreen
    currentScreen = 'Main'
    viewHand()

'''call countCards after making changes to playerHand'''
def countCards():
    #reset counts
    global player1Counts, player2Counts
    player1Counts, player2Counts = [0] * 8, [0] * 8

    #count number of cards
    if turn.p_turn == 1: 
        for i in player1Hand:
            player1Counts[card.Card.cardType[i.action]] += 1
    else:
        for i in player2Hand:
            player2Counts[card.Card.cardType[i.action]] += 1

def numberMatches():
    # Reset counts
    global p1_tablecounts, p2_tablecounts
    p1_tablecounts,p2_tablecounts = [0] * 3, [0] * 3
    
    # For each of the different values, add one
    p1_match = [0,0,0]
    if turn.p_turn == 1:
        for m in player1Matches:
            if m.action == '25':
                p1_match[0] += 1
            elif m.action == '50':
                p1_match[1] += 1
            else:
                p1_match[2] += 1

    # Divide each one by two, since 2 cards only count as one value 
        for amount in range(len(p1_match)):
            p1_match[amount] = (p1_match[amount]) // 2
            p1_tablecounts[amount] += p1_match[amount]

    # Repeat for opposite player
    else:
        p2_match = [0,0,0]
        for m in player2Matches:
            if m.action == '25':
                p2_match[0] += 1
            elif m.action == '50':
                p2_match[1] += 1
            else:
                p2_match[2] += 1

        for amount in range(len(p2_match)):
            p2_match[amount] = (p2_match[amount]) // 2
            p2_tablecounts[amount] += p2_match[amount]

# Function for calculating score
def calculatescore(playerMatches):
    # list of how may of each we have
    playerTableCount = [0, 0, 0]

    # For each of the different values, add one

    for m in playerMatches:
        if m == '25':
            playerTableCount[0] += 1
        elif m == '50':
            playerTableCount[1] += 1
        else:
            playerTableCount[2] += 1

    # Divide each one by two, since 2 cards only count as one value
    newPlayerTableCount = []
    for amount in playerTableCount:
        amount = amount // 2
        newPlayerTableCount.append(amount)

    # Turn values into a score
    return (((newPlayerTableCount[0])*25)+((newPlayerTableCount[1])*50)+((newPlayerTableCount[2])*100))

def useCard(playerCounts, playerMatches, playerHand, key): #pass player's hand depending on whos turn it is
    # for event in pygame.event.get():
    #     if(event.type == pygame.KEYDOWN):

            #trying to use currency cards
            global player1Score,player2Score
            
            if(key == pygame.K_a):
                if(playerCounts[0] > 1): #player has more than 1 of low tier card
                    #loop through player's hand to find low tier card
                    count = 0
                    for i, c in enumerate(playerHand):
                        if(count < 2):
                            if(c.action == '25'):
                                playerMatches.append(playerHand.pop(i))
                                #playerHand.pop(c)
                                count += 1
                        #elif(count >= 2):
                         #   break
                else:
                    #player does not have enough cards
                    print("insufficient cards")
                if(turn.p_turn == 1): player1Score = calculatescore(playerMatches)
                else: player2Score = calculatescore(playerMatches)
                endGame(False)
            if(key == pygame.K_b):
                if(playerCounts[1] > 1): #player has more than 1 of med tier card
                    #loop through player's hand to find med tier card
                    count = 0
                    for i, c in enumerate(playerHand):
                        if(count < 2):
                            if(c.action == '50'):
                                playerMatches.append(playerHand.pop(i))
                                #playerHand.pop(c)
                                count += 1
                        #else:
                           # break
                else:
                    #player does not have enough cards
                    print("insufficient cards")
                if(turn.p_turn == 1): player1Score = calculatescore(playerMatches)
                else: player2Score = calculatescore(playerMatches)
                endGame(False)
            if(key == pygame.K_c):
                if(playerCounts[2] > 1): #player has more than 1 of high tier card
                    #loop through player's hand to find high tier card
                    count = 0
                    for i, c in enumerate(playerHand):
                        if(count < 2):
                            if(c.action == '100'):
                                playerMatches.append(playerHand.pop(i))
                                #playerHand.pop(c)
                                count += 1
                        #else:
                        #    break
                else:
                    #player does not have enough cards
                    print("insufficient cards")
                if(turn.p_turn == 1): player1Score = calculatescore(playerMatches)
                else: player2Score = calculatescore(playerMatches)
                endGame(False)
            #trying to use action cards
            
            if(key == pygame.K_d):
                if(playerCounts[3] > 0): #player has 
                    #pop this action card, skip next player
                    popCard('Skip', playerHand)
                    skipNextPlayer()
                else:
                    #player does not have 
                    print("insufficient cards")
            if(key == pygame.K_e):
                if(playerCounts[4] > 0): #player has
                    #pop this action card, steal money
                    popCard('Steal Money', playerHand)
                    stealMoney()
                else:
                    #player does not have
                    print("insufficient cards")
                if(turn.p_turn == 1): player1Score = calculatescore(playerMatches)
                else: player2Score = calculatescore(playerMatches)
                endGame(False)
            if(key == pygame.K_f):
                if(playerCounts[5] > 0): #player has 
                    #pop this action card, steal card
                    popCard('Steal Card', playerHand)
                    stealCard()
                else:
                    #player does not have 
                    print("insufficient cards")
            if(key == pygame.K_g):
                if(playerCounts[6] > 0): #player has 
                    #pop this action card, trade
                    popCard('Trade', playerHand)
                    trade(playerHand)
                else:
                    #player does not have 
                    print("insufficient cards")
            if(key == pygame.K_h):
                if(playerCounts[7] > 0): #player has
                    #pop this action card, draw2
                    popCard('Draw 2', playerHand)
                    drawCards(playerHand)
                else:
                    #player does not have
                    print("insufficient cards")

def popCard(identity, playerHand):
    popped = False
    for i, c in enumerate(playerHand):
        if(popped == False):
            if(c.action == identity):
                playerHand.pop(i)
                popped = True
        else: break

def skipNextPlayer():
    #sets the turn back to whoever's turn it is
    if(turn.p_turn == 1):
        turn.p_turn = 2
        turn.nextTurn()
        moves = 3
    else:
        turn.p_turn = 1
        turn.nextTurn()
        moves = 3

def stealMoney():
    #steal randomly (25, 50, 100) from opponent
    pickup = random.randint(0, 2)
    
    if(turn.p_turn == 1): miniStealMoney(player1Money, player2Money, pickup)
    else: miniStealMoney(player2Money, player1Money, pickup)

def miniStealMoney(m_player, m_otherPlayer, index):
    #check if other player has specified amount on table
    if(m_otherPlayer[index] > 0):
        m_player[index] += 1
        m_otherPlayer[index] -= 1
    #else do nothing

def stealCard(playerGain, playerLose):
    #steal 2 cards randomly from opponent
        #first player will gain while the second player loses from their deck
    for i in range(2):
        randCard = random.randint(0, len(playerLose)-1)
        playerGain.append(playerLose.pop(randCard))
    pass

def trade(playerHand):
    #player chooses 2 cards they want to trade in (Gets removed from the players hand and put in deck)
    #they get 2 random cards from the deck

    #get index of each card
    index1 = getIndex()
    index2 = getIndex()
    #add 2 cards to the deck from the player's hand
    deck.cards.append(playerHand.pop(index1))
    deck.cards.append(playerHand.pop(index2))
    #call the draw cards function
    drawCards(playerHand)

def getIndex():
    if(event.key == pygame.K_a):
        return 0
    if(event.key == pygame.K_b):
        return 1
    if(event.key == pygame.K_c):
        return 2
    if(event.key == pygame.K_d):
        return 3
    if(event.key == pygame.K_e):
        return 4
    if(event.key == pygame.K_f):
        return 5
    if(event.key == pygame.K_g):
        return 6
    if(event.key == pygame.K_h):
        return 7

def drawCards(playerHand):
    #add 2 cards from the deck to playerHand
    for i in range(2):
        if(len(deck.cards) == 0):
            endGame(True)
            break
        playerHand.append(deck.cards.pop(random.randint(0, len(deck.cards) - 1)))

def endGame(isDeckEmpty):
    #if either player gets the score cap of 700
    #if deck runs out, player with higher score
    global currentScreen

    if(isDeckEmpty == False):
        if(player1Score >= 700):
            #display player 1 win
            screen.blit(pygame.image.load('./images/player1Win.png'), (0, 0))
            currentScreen = 'End'
        if(player2Score >= 700):
            #display player 2 win
            screen.blit(pygame.image.load('./images/player2Win.png'), (0, 0))
            currentScreen = 'End'
    else:
        currentScreen = 'End'
        if(player1Score > player2Score):
            #display player 1 win
            screen.blit(pygame.image.load('./images/player1Win.png'), (0, 0))
        elif (player2Score > player1Score):
            #display player 2 win
            screen.blit(pygame.image.load('./images/player2Win.png'), (0, 0))
        else:
            #display tie
            screen.blit(pygame.image.load('./images/tie.png'), (0, 0))


def viewDefault():
    #the things that are always on the screen
    GAME_FONT.render_to(screen, (340, 157), f'{len(deck.cards)}', (104, 202, 244))
    GAME_FONT.render_to(screen, (790, 230), f'{moves}', (104, 202, 244))
    if turn.p_turn == 1:
        GAME_FONT.render_to(screen, (330, 777), f'{player1Score}', (104, 202, 244))
        GAME_FONT.render_to(screen, (330, 969), f'{player2Score}', (104, 202, 244))
    else:
        GAME_FONT.render_to(screen, (330, 777), f'{player2Score}', (104, 202, 244))
        GAME_FONT.render_to(screen, (330, 969), f'{player1Score}', (104, 202, 244))

def viewHand(): 
    #background
    screen.blit(pygame.image.load('./images/hand' + f'{turn.p_turn}' + '.png'), (0,0))

    viewDefault()
    countCards()

    #amount of each card
    if turn.p_turn == 1:
        for i in range(len(player1Counts)):
            GAME_FONT.render_to(screen, cardCountLocations[i], f'{player1Counts[i]}', (104, 202, 244))
    else:
        for i in range(len(player2Counts)):
            GAME_FONT.render_to(screen, cardCountLocations[i], f'{player2Counts[i]}', (104, 202, 244))

def viewTable(yourMatch,opponentMatch):
    #background
    screen.blit(pygame.image.load('./images/table' + f'{turn.p_turn}' + '.png'), (0,0))

    numberMatches()
    viewDefault()

    # Put current players stuff on screen
    for i in range(len(yourMatch)):
        GAME_FONT.render_to(screen,tableCardCountLocations[0][i], f'{yourMatch[i]}', (104, 202, 244))
    # Put opponent's stuff on screen
    for i in range(len(opponentMatch)):
        GAME_FONT.render_to(screen, tableCardCountLocations[1][i], f'{opponentMatch[i]}', (104, 202, 244))

def viewInstructions():
    global currentScreen
    currentScreen = 'Instructions'
    screen.blit(pygame.image.load('./images/instructions.png'), (0, 0))

def viewTitle():
    global currentScreen
    currentScreen = 'Title'
    screen.blit(pygame.image.load('./images/title.png'), (0,0))
    
#init player hands
for i in range(5):
    player1Hand.append(deck.cards.pop(random.randint(0, len(deck.cards)-1)))
    player2Hand.append(deck.cards.pop(random.randint(0, len(deck.cards)-1)))
countCards()

viewTitle()

finalturn = 2
#game loop
while 1:
    
    actions = [pygame.K_a, pygame.K_b, pygame.K_c, pygame.K_d, pygame.K_e, pygame.K_f, pygame.K_h]

    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                sys.exit()
            elif event.key == pygame.K_1 and currentScreen == 'Main':
                moves = 0
            elif event.key in actions and currentScreen == 'Main':
                moves -= 1
                countCards()
                if(turn.p_turn == 1):
                    useCard(player1Counts, player1Matches, player1Hand, event.key)
                else:
                    useCard(player2Counts, player2Matches, player2Hand, event.key)
                if currentScreen == 'Main':
                    viewHand()
            elif event.key == pygame.K_UP and currentScreen == 'Main':
                viewHand()
            elif event.key == pygame.K_DOWN and currentScreen == 'Main':
                viewTable(p1_tablecounts, p2_tablecounts)
            elif event.key == pygame.K_RETURN and currentScreen == 'Title':
                startGame()
            elif event.key == pygame.K_TAB:
                if currentScreen == 'Title':
                    viewInstructions()
                elif currentScreen == 'Instructions':
                    viewTitle()

    #player out of moves
    if moves <= 0:
        moves = 3
        turn.nextTurn()
        #draw up to 3 cards, limit 15
        if turn.p_turn == 1:
            if len(deck.cards) == 0:
                finalturn -= 1
            else:
                for i in range(min(3, 15-len(player1Hand))):
                    drawCards(player1Hand)
                    #player1Hand.append(deck.cards.pop(random.randint(0, len(deck.cards)-1)))
                else: print('else with a for loop is cool')
            countCards()
        else:
            if len(deck.cards) == 0:
                finalturn -= 1
            else:
                for i in range(min(3, 15-len(player2Hand))):
                    drawCards(player2Hand)
                    #player2Hand.append(deck.cards.pop(random.randint(0, len(deck.cards)-1)))
            countCards()
        viewHand()
        
    if finalturn == 0: #deck is empty and players have done final turns
        endGame(True)

    pygame.display.flip()