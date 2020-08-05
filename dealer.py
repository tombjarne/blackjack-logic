class Dealer:
    name = ""
    cards = []
    cardStack = []

    def __init__(self, name):
        self.name = name

    def setcardstack(self, stack):
        self.cardStack = stack

    def drawcard(self):
        current = self.cardStack.pop()
        self.cards.append(current)
        del self.cardStack[-1]
        return current

    def dealcard(self, player):
        current = self.cardStack.pop()
        player.cards.append(current)
        del self.cardStack[-1]
        return current

    def getallcards(self):
        return self.cardStack
