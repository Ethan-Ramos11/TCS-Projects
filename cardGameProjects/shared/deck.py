from classes.card import Card

import random


class Deck:
    def __init__(self, numDecks):
        self.deck = []
        self.buildDecks(numDecks)
        self.discard = []

    def buildDecks(self, numDecks):
        if numDecks <= 0:
            numDecks = 1
        suits = ["♠", "♥", "♦", "♣"]
        ranks = [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"]
        for _ in len(numDecks):
            for suit in suits:
                for rank in ranks:
                    self.deck.append(Card(suit, rank))

    def printDeck(self):
        for card in self.deck:
            print(card)

    def draw(self):
        if self.deck:
            card = self.deck.pop()
            return card
        else:
            print("No more cards are left")
            return None

    def discardCard(self, card):
        self.discard.append(card)

    def shuffle(self):
        random.shuffle(self.deck)

    def rebuildDeck(self):
        for card in self.discard:
            self.deck.append(card)
        self.discard = []

    def dealCards(self, players, handLength):
        if handLength * len(players) > len(self.deck):
            print("Not enough cards in the deck")

        for player in players:
            card = self.draw()
            player.addCard(card)
