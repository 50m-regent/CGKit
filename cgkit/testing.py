from data.player_data import PlayerData
from scaffolds.game import Game
from scaffolds.player import Player
from scaffolds.card import Card

if __name__ == '__main__':
    player1 = Player()
    player2 = Player()

    game = Game(players=[player1, player2])