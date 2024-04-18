import random
class Card():
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
    def __str__(self):
        rank = ""
        if self.rank == 1:
            rank = "Ace"
        elif self.rank == 11:
            rank = "Jack"
        elif self.rank == 12:
            rank = "Queen"
        elif self.rank == 13:
            rank = "King"
        else:
            rank = (self.rank)
        return rank + " of " + self.suit
    SUITS = ['Hearts', 'Spades', 'Clubs', 'Diamonds']
    RANKS = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
class Deck():
    def __init__(self):
        self.cards = []
        for suit in Card.SUITS:
            for rank in Card.RANKS:
                self.cards.append(Card(rank, suit))
    
    def __len__(self):
        return len(self.cards)
    
    def __str__(self):
        result = ""
        for c in self.cards:
            result += str(c) + "\n"
        return result
    
    def shuffle(self):
        random.shuffle(self.cards)
    
    def deal(self):
        if len(self) > 0:
            return self.cards.pop(0)
        else:
            return None