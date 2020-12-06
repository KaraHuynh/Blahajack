import pygame

p1_tablecounts = [0] * 3
p2_tablecounts = [0] * 3
# player1Matches,player2Matches = ['25','25','100','100','100','100'],['50','50','25','25','100','100','100','100']

def numberMatches():
    # Reset counts
    global p1_tablecounts, p2_tablecounts
    p1_tablecounts, p2_tablecounts = [],[]

    # For each of the different values, add one
    p1_match = [0, 0, 0]
    if turn.p_turn == 1:
        for m in player1Matches:
            if m == '25':
                p1_match[0] += 1
            elif m == '50':
                p1_match[1] += 1
            else:
                p1_match[2] += 1

        # Divide each one by two, since 2 cards only count as one value
        for amount in p1_match:
            p1_tablecounts.append(amount//2)

    # Repeat for opposite player
    else:
        p2_match = [0, 0, 0]
        for m in player2Matches:
            if m == '25':
                p2_match[0] += 1
            elif m == '50':
                p2_match[1] += 1
            else:
                p2_match[2] += 1

        for amount in p2_match:
            p2_tablecounts.append(amount//2)





