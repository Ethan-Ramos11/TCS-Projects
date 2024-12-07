from shared.card import Card


class Player:
    def __init__(self, name):
        self.name = name
        self.cardCount = self.buildCardCount()
        self.hand = []
        self.bookedSets = []

    def buildCardCount(self):
        hand = {}
        ranks = [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"]
        for rank in ranks:
            hand[rank] = 0
        return hand

    def addCard(self, card):
        self.hand.append(card)
        self.cardCount[card.getRank] += 1

    def askForCard(self, player, card, deck):
        if card in player.hand and player.hand[card] > 0:
            self.hand[card] = self.hand.get(card) + player.hand[card]
            player.hand[card] = 0
            if self.hand[card] == 4:
                del self.hand[card]
                self.bookedSets.append(card)
        else:
            card = deck.draw()
            print(card)
            if card.getRank() in self.hand:
                self.hand[card.getRank()] += 1
            print("Go fish")
