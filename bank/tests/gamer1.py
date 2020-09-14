class Player:
    def __init__(self, sign):
        self.sign = sign

    def __str__(self):
        return "Игрок {}".format(self.sign)
