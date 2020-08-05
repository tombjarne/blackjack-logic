from card import Card

class CardStack:
    cardStack = []
    symbols = [
        "diamond",
        "clubs",
        "heart",
        "spades",
    ]
    names = [
        "1",
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
        "10",
        "Jack",
        "Queen",
        "King",
        "Ace"
    ]
    numbers = [
        1,
        2,
        3,
        4,
        5,
        6,
        7,
        8,
        9,
        10,
        11
    ]

    def __init__(self):
        self.createCards()

    def createcards(self):
        for i in range(1, 10, 1):
            self.cardStack.append(Card("Diamond " + i, "Diamond", i, False))

        self.cardStack.append(Card("Diamond Jack", "Diamond", 10, False))
        self.cardStack.append(Card("Diamond Queen", "Diamond", 10, False))
        self.cardStack.append(Card("Diamond King", "Diamond", 10, False))
        self.cardStack.append(Card("Diamond Ace", "Diamond", 11, True))

        for i in range(1, 10, 1):
            self.cardStack.append(Card("Clubs " + i, "Clubs", i, False))

        self.cardStack.append(Card("Clubs Jack", "Clubs", 10, False))
        self.cardStack.append(Card("Clubs Queen", "Clubs", 10, False))
        self.cardStack.append(Card("Clubs King", "Clubs", 10, False))
        self.cardStack.append(Card("Clubs Ace", "Clubs", 11, True))

        for i in range(1, 10, 1):
            self.cardStack.append(Card("Heart " + i, "Heart", i, False))

        self.cardStack.append(Card("Heart Jack", "Heart", 10, False))
        self.cardStack.append(Card("Heart Queen", "Heart", 10, False))
        self.cardStack.append(Card("Heart King", "Heart", 10, False))
        self.cardStack.append(Card("Heart Ace", "Heart", 11, True))

        for i in range(1, 10, 1):
            self.cardStack.append(Card("Spades " + i, "Spades", i, False))

        self.cardStack.append(Card("Spades Jack", "Spades", 10, False))
        self.cardStack.append(Card("Spades Queen", "Spades", 10, False))
        self.cardStack.append(Card("Spades King", "Spades", 10, False))
        self.cardStack.append(Card("Spades Ace", "Spades", 11, True))
