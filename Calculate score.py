import pygame

# Function for calculating score
def calculatescore(playerScore,playerMatches):
    # list of how may of each we have
    playerTableCount = [0, 0, 0]

    # For each of the different values, add one

    for i, m in enumerate(playerMatches):
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
    playerScore += (((newPlayerTableCount[0])*25)+((newPlayerTableCount[1])*50)+((newPlayerTableCount[2])*100))

# Calling the function
# If player 1's turn
if (turn.p_turn == 1):
    calculatescore(player1Score,player1Matches)
# If player 2's turn
else:
    calculatescore(player2Score,player2Matches)
