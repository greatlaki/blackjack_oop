import player
from deck import Deck
from const import MESSAGES

import random


class Game:

    max_pl_count = 4

    def __init__(self):
        self.players = []
        self.player = None
        self.player_pos = None
        self.dealer = player.Dealer()
        self.all_players_count = 1
        self.deck = Deck()
        self.max_bet, self.min_bet = 20, 0

    @staticmethod
    def _ask_starting(message):
        while True:
            choice = input(message)
            if choice == 'n':
                return False
            elif choice == 'y':
                return True

    def _launching(self):
        while True:
            bots_count = int(input("Hello, write bots count "))
            if bots_count <= self.max_pl_count - 1:
                break
            self.all_players_count = bots_count + 1

        for _ in range(bots_count):
            b = player.Bot()
            self.players.append(b)

            print(b, ' is created')

        self.player = player.Player()
        self.player_pos = random.randint(0, self.all_players_count)
        print("Your position is:", self.player_pos)
        self.players.insert(self.player_pos, self.player)

    def ask_bet(self):
        for player in self.players:
            player.change_bet(self.max_bet, self.min_bet)

    def first_descr(self):
        for player in self.players:
            for _ in range(2):
                card = self.deck.get_card()
                player.take_card(card)

        card = self.deck.get_card()
        self.dealer.take_card(card)
        self.dealer.print_cards()

    def check_stop(self, player):
        if player.full_points >= 21:
            return True
        else:
            return False

    def remove_player(self, pl):
        pl.print_cards()
        if isinstance(pl, player.Player):
            print('You are fall!')
        if isinstance(pl, player.Bot):
            print(pl, 'are fall!')
        self.players.remove(pl)

    def ask_cards(self):
        for pl in self.players:

            while pl.ask_card():
                card = self.deck.get_card()
                pl.take_card(card)

                is_stop = self.check_stop(pl)
                if is_stop:
                    if pl.full_points > 21 or isinstance(pl, player.Player):
                        self.remove_player(pl)
                    break

                if isinstance(pl, player.Player):
                    pl.print_cards()

    def check_winner(self):
        if self.dealer.full_points > 21:
            # all win
            print("Dealer are fall! ALL players in game are win!")
            for winner in self.players:
                winner.money += winner.bet * 2
        else:
            for pl in self.players:
                if pl.full_points == self.dealer.full_points:
                    pl.money += pl.bet
                    print(MESSAGES.get('eq').format(player=pl,
                                                    points=pl.full_points))
                elif pl.full_points > self.dealer.full_points:
                    pl.money += pl.bet * 2
                    if isinstance(pl, player.Bot):
                        print(MESSAGES.get('win').format(pl))
                    elif isinstance(pl, player.Player):
                        print("You are win")

    def play_with_dealer(self):
        while self.dealer.ask_card():
            card = self.deck.get_card()
            self.dealer.take_card(card)
        self.dealer.print_cards()

    def start_game(self):
        message = MESSAGES.get('ask_start')
        # todo: max players count?
        if not self._ask_starting(message=message):
            exit(1)

        # generating data rof starting
        self._launching()

        # ask about bet
        self.ask_bet()

        # give first cards to the players
        self.first_descr()

        # print player cards after first deal
        self.player.print_cards()

        # ask players about cards
        self.ask_cards()

        self.play_with_dealer()