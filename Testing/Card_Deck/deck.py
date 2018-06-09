"""
The class that will represent the Deck.
"""

from .card import Card


class Deck(object):
    def __init__(self, colors, cards, specials=None):
        self.structure = set()
        self.colors = colors
        self.cards = cards
        self.specials = specials if specials is not None else None
        self.random_card = None

    def build_deck(self):
        for card in self.cards:
            for color in self.colors:
                self.structure.add(Card(color, card))

        if self.specials is not None:
            for special in self.specials:
                self.structure.add(Card(special[0], special[1]))

    def get_card(self):
        self.random_card = self.structure.pop()
        self.structure.add(self.random_card)
        return self.structure.pop()


