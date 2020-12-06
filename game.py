import sys, pygame, random, card, deck, turn
import pygame.freetype

#init pygame
pygame.init()

size = width, height = 1920, 1080
screen = pygame.display.set_mode(size)
black = 0, 0, 0
white = 255, 255, 255
GAME_FONT = pygame.freetype.Font("./images/comicsans.ttf", 36)

#functions
def myHand():
    #show cards the player has
    choice = input("press key A to O to select a card (1-15):\n")
    choice = (ord(choice) % 96) % 64
    print(choice)

def putCurrencyDown():
    print("putting currency down")

def viewHand():
    screen.blit(pygame.image.load('./images/hand' + f'{turn.p_turn}' + '.png'), (0,0))

    nlow = 0
    nmed = 0
    nhigh = 0
    nskip = 0
    nstealm = 0
    nstealc = 0
    ntrade = 0
    ndraw = 0

    counts = [0] * 8
    cardCountLocations = [(604, 634), (935, 634), (1310, 634), (1668, 634), (607, 1039), (945, 1039), (1337, 1039), (1698, 1039)]

    #deck location 315, 162
    #your money 280, 784
    #their money 274, 981
    #turns left 751, 238

    if turn.p_turn == 1:
        for i in player1Hand:
            counts[card.Card.cardType[i.action]] += 1
    else:
        for i in player2Hand:
            counts[card.Card.cardType[i.action]] += 1

    #print text at 564, 651
    for i in range(len(counts)):
        GAME_FONT.render_to(screen, cardCountLocations[i], f'{counts[i]}', (104, 202, 244))

def viewTable():
    screen.blit(pygame.image.load('./images/table' + f'{turn.p_turn}' + '.png'), (0,0))

    #their low 547, 498
    #their med 1003, 496
    #their high 1458, 499
    #your low 544, 873
    #your med 1000, 888
    #your high 1459, 886

#init game stuff

turn = turn.Turn(random.randint(1, 2))

player1Score = 0
player2Score = 0

deck = deck.Deck()
deck.reset()
print(f' size of deck {len(deck.cards)}')
deck.shuffle()
player1Hand = []
player2Hand = []
player1Matches = []
player2Matches = []

#init player hands
for i in range(5):
    player1Hand.append(deck.cards.pop(random.randint(0, len(deck.cards)-1)))
    player2Hand.append(deck.cards.pop(random.randint(0, len(deck.cards)-1)))

#setup display
viewHand()

#game loop
test = 0
while 1:
    test += 1
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

        if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    sys.exit()
                elif event.key == pygame.K_1:
                    turn.nextTurn()
                elif event.key == pygame.K_2:
                    choice = 2
                elif event.key == pygame.K_UP:
                    viewHand()
                elif event.key == pygame.K_DOWN:
                    viewTable()

    
    # refresh screen for next turn
    # x = 0
    # y = 0
    # for i, j in enumerate(player1Hand):
    #     screen.blit(pygame.image.load(j.image), (x,y))
    #     x += 100
    #     y += 100
    #     if i % 5 == 0:
    #         x += 100
    #         y = 0

    print(f'window loop, {test}')

    pygame.display.flip()