# coding=utf-8
# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from card import Card
from cardstack import CardStack
from dealer import Dealer
from player import Player


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print("Hi, {0}".format(name))  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    newcard = Card("Testkarte", "Symbol", 3, False)
    print(newcard.getsymbol())

    player = Player("Tom")
    player.setbet(1)
    print(player.setbet(5))
    dealer = Dealer("Dealer")
    cardStack = CardStack()

    dealer.setcardstack(cardStack.cardStack)

    print(dealer.getallcards())
    print(dealer.drawcard().getname())

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
