import pygame


def number_Matches(player1Matches,player2Matches):

    # For each of the different values, add one

    for i, m in enumerate(player1Matches):
        if m == '25':
            p1_tablecounts[0] += 1
        elif m == '50':
            p1_tablecounts[1] += 1
        else:
            p1_tablecounts[2] += 1

            # Divide each one by two, since 2 cards only count as one value

    for amount in p1_tablecounts:
        amount = amount // 2

    # Repeat for opposite player

    for i, m in enumerate(player2Matches):
        if m == '25':
            p2_tablecounts[0] += 1
        elif m == '50':
            p2_tablecounts[1] += 1
        else:
            p2_tablecounts[2] += 1

    for amount in p2_tablecounts:
        amount = amount // 2

def viewTable():
    #background
    screen.blit(pygame.image.load('./images/table' + f'{turn.p_turn}' + '.png'), (0,0))

    number_Matches()
    viewDefault()

    # Put player 1's stuff onto screen
    print(f'p1cPRINTING:{player1Counts}')
    for i in range(len(p1_tablecounts))

    #their low 547, 498
    #their med 1003, 496
    #their high 1458, 499
    #your low 544, 873
    #your med 1000, 888
    #your high 1459, 886



