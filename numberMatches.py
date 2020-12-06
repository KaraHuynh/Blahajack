import pygame

def numberMatches(player1Matches,player2Matches):
    # Reset counts
    global p1_tablecounts, p2_tablecounts
    p1_tablecounts,p2_tablecounts = [0] * 3,[0] * 3
    
    # For each of the different values, add one
    p1_match = [0,0,0]
    for m in player1Matches:
        if m == '25':
            p1_match[0] += 1
        elif m == '50':
            p1_match[1] += 1
        else:
            p1_match[2] += 1

    # Divide each one by two, since 2 cards only count as one value
    for amount in range(len(p1_match)):
        p1_match[amount] = (p1_match[amount]) // 2
        p1_tablecounts[amount] += p1_match[amount]

    # Repeat for opposite player
    p2_match = [0,0,0]
    for m in player2Matches:
        if m == '25':
            p2_match[0] += 1
        elif m == '50':
            p2_match[1] += 1
        else:
            p2_match[2] += 1

    for amount in range(len(p2_match)):
        p2_match[amount] = (p2_match[amount]) // 2
        p2_tablecounts[amount] += p2_match[amount]

