class Player:
    name = ""
    bank = 0
    bet = 5
    cards = []
    split = False
    double = False

    def __init__(self, name):
        self.name = name

    def getbank(self):
        return self.bank

    def getbet(self):
        return self.bet

    def getname(self):
        return self.name

    def setbank(self, value):
        self.bank += value

    def setbet(self, value):
        if value >= 5 and self.bank >= 5:
            self.bet += value
            self.bank -= value
            return True
        else:
            return False

    def setcard(self, card):
        self.cards.append(card)

    def getcards(self):
        return self.cards

    def setdouble(self, double):
        self.double = double

    def setsplit(self, split):
        self.double = split
