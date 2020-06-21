class Player:
    def __init__(self, data=None):
        if data == None:
            self.id   = 0
            self.name = 'unnamed'

            self.status = {}

            self.deck = []

        else:
            self.id   = data.id
            self.name = data.name

            self.status = data.status

            self.deck = data.deck