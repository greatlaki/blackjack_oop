import abc

from deck import Deck

class AbstractPlayer(abc.ABC):

    def __init__(self, position):
        self.cards = []
        self.position = position

    def ask_card(self, deck):
        card = deck.get_card()
        self.cards.append(card)
        return True


class Player(AbstractPlayer):
    pass


class Dealer(AbstractPlayer):
    pass


class Bot(AbstractPlayer):

    def __init__(self):
