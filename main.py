from deck import Deck
from game import Game

from player import Bot

if __name__ == '__main__':
    g = Game()
    g.start_game()

    print(g.player.money)
    # for pl in g.players:
    #     pl.print_cards()
    #     if isinstance(pl, Bot):
    #         print('Max points: ', pl.max_points)
    #     print('*********')