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


