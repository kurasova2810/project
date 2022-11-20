
class NoHealth(Exception):
    def __init__(self, health):
            self.health = health

class NoMood(Exception):
    def __init__(self, mood):
            super().__init__(mood)


class NoMoney(Exception):
    def __init__(self, money):
        super().__init__(money)
