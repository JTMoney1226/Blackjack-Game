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

class Player():
    def __init__(self, cards = []):
        self.cards = cards
    
    def __str__(self):
        result = ""
        for c in self.cards:
            result += str(c) + " "
        result += "\n" + str(self.getPoints())
        return result
    
    def hit(self, card):
        self.cards.append(card)

    def getPoints(self):
        score = 0
        for card in self.cards:
            if card.rank == "Ace":
                score += 11
            elif card.rank > "9":
                score += 10
            else:
                score += int(card.rank)
        
        for card in self.cards:
            if score > 21:
                if card.rank == "Ace":
                    score -= 10
        return score
    
    def hasBlackJack(self):
        return len(self.cards) == 2 and self.getPoints() == 21
    
class Dealer(Player):
    def __init__(self, cards = []):
        Player.__init__(self, cards)
        self.showOneCard = True

    def __str__(self):
        if self.showOneCard:
            return str(self.cards[0])
        else:
            return Player.__str__(self)
    
    def hit(self, deck):
        self.showOneCard = False
        while self.getPoints() < 17:
            self.cards.append(deck.deal())
            
class Blackjack():
    def __init__(self):
        self.deck = Deck()
        self.deck.shuffle()
        # pass player and dealer cards
        self.player = Player([self.deck.deal(), self.deck.deal()])
        self.dealer = Dealer([self.deck.deal(), self.deck.deal()])
    
    def play(self):
        print("Player:\n", self.player)
        print("Dealer:\n", self.dealer)
        #Player hits until NO
        while True:
            choice = input("Do you want to hit? [y/n]")
            if choice in ("Y", "y"):
                self.player.hit(self.deck.deal())
                points = self.player.getPoints()
                print("Player:\n", self.player)
                if points >= 21:
                    break
            else:
                playerPoints = self.player.getPoints()
                if playerPoints > 21:
                    print("You bust and lose")
                else:
                #Dealer's turn
                    self.dealer.hit(self.deck)
                    print("Dealer:\n", self.dealer)
                    dealerPoints = self.dealer.getPoints()
                    if dealerPoints > 21:
                        print("Dealer busts and you win!")
                    elif dealerPoints > playerPoints:
                        print("Dealer wins!")
                    elif playerPoints > dealerPoints and playerPoints <= 21:
                        print("You win!")
                    elif dealerPoints == playerPoints:
                        if self.player.hasBlackJack() and not self.dealer.hasBlackJack():
                            print("You win!")
                        elif not self.player.hasBlackJack() and self.dealer.hasBlackJack():
                            print("Dealer wins!")
                        else:
                            print("There is a tie!")
                break

if __name__ == "__main__":
    game = Blackjack()
    game.play()