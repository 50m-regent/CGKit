from random import randint

class Game:
    def __init__(self, players=[]):
        self.players = players

    def init(self):
        self.turn = randint(0, len(players) - 1)