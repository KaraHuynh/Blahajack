class Card:

    cardType = {'25': 0, '50': 1, '100': 2, 'Skip': 3, 'Steal Money': 4, 'Steal Card': 5, 'Trade': 6, 'Draw 2': 7}

    def __init__(self, value, action, image): #, desc):
        self.val = value
        self.action = action
        self.image = image
        #self.desc = desc