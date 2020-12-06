
# their low 547, 498
# their med 1003, 496
# their high 1458, 499
# your low 544, 873
# your med 1000, 888
# your high 1459, 886

def viewTable(yourMatch,opponentMatch):
    #background
    screen.blit(pygame.image.load('./images/table' + f'{turn.p_turn}' + '.png'), (0,0))

    numberMatches(player1Matches,player2Matches)
    viewDefault()

    # Put current players stuff on screen
    for i in range(len(yourMatch)):
        GAME_FONT.render_to(screen,tableCardCountLocations[0][i], f'{yourMatch[i]}', (104, 202, 244))
    # Put opponent's stuff on screen
    for i in range(len(opponentMatch)):
        GAME_FONT.render_to(screen, tableCardCountLocations[1][i], f'{opponentMatch[i]}', (104, 202, 244))

# Calling function
# if it is player 1's turn
if (turn.p_turn == 1):
    viewTable(p1_tablecounts,p2_tablecounts)
# if it is player 2's turn
else:
    viewTable(p2_tablecounts,p1_tablecounts)

