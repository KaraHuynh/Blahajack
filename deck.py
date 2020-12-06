import card, random

class Deck:

    def __init__(self):
        self.cards = []
    
    def reset(self):
        self.cards.clear()
        for i in range(75):
            if i < 20:
                self.cards.append(card.Card(25, '25', './images/low.png',))# '25 dollar'))
            elif i < 40:
                self.cards.append(card.Card(50, '50', './images/med.png',))# '50 dollar'))
            elif i < 50:
                self.cards.append(card.Card(100, '100', './images/high.png',))# '100 dollar'))
            elif i < 55:
                self.cards.append(card.Card(0, 'Skip', './images/skip.png',))# 'Skips the other players turn'))
            elif i < 60:
                self.cards.append(card.Card(0, 'Steal Money', './images/stealm.png',))# 'Steals money from the other player'))
            elif i < 65:
                self.cards.append(card.Card(0, 'Steal Card', './images/stealc.png',))# 'Steals a card from the other player'))
            elif i < 70:
                self.cards.append(card.Card(0, 'Trade', './images/trade.png'))#, 'Trade 2 cards with the other player'))
            else:
                self.cards.append(card.Card(0, 'Draw 2', './images/draw.png'))#, 'Draw 2 cards from the deck'))

    def shuffle(self):
        random.shuffle(self.cards)