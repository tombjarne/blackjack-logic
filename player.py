class Player:
    name = ""
    bank = 0
    bet = 0
    cards = []
    split = False
    double = False

    def __init__(self, name, bank, bet):
        self.name = name
        self.bank = bank
        self.bet = bet

    def getbank(self):
        return self.bank

    def getbet(self):
        return self.bet

    def getname(self):
        return self.name

    def setbank(self, value):
        self.bank += value

    def setbet(self, value):
        self.bet += value

    def setcard(self, card):
        self.cards.append(card)

    def getcards(self):
        return self.cards

    def setdouble(self, double):
        self.double = double

    def setsplit(self, split):
        self.double = split
