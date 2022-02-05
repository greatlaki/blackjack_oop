from deck import Deck
from game import Game

if __name__ == '__main__':
    g = Game()
    g.start_game()

    for pl in g.players:
        pl.print_cards()
        print("***************")

    print(g.player_pos)
    print(g.players)