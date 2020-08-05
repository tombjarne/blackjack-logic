from dealer import Dealer
from player import Player

class GameController:
    def __init__(self):
        pass

    def startgame(self):
        player = Player("default", 0, 0)
        dealer = Dealer("Dealer")
