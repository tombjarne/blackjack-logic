class Card:

    name = ""
    symbol = ""
    value = 0
    ace = False

    def __init__(self, name, symbol, value, ace):
        self.name = name
        self.symbol = symbol
        self.value = value
        self.ace = ace

    def getsymbol(self):
        return self.symbol

    def getvalue(self):
        return self.value

    def getace(self):
        return self.ace

    def getname(self):
        return self.name
