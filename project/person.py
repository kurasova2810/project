from errors import NoHealth
from errors import NoMood
from errors import NoMoney

class Person:
    name = ''
    health = 100
    mood = 100
    money = 0

    def __init__(self, name='', health=100, mood=100, money=0):
        self.name = name
        self.health = health
        self.mood = mood
        self.money = money

    def __str__(self):
        return f'== {self.name} ==\n' \
               f'Здоровье: {self.health}\n' \
               f'Настроение: {self.mood}\n' \
               f'Деньги: {self.money}\n'

    def health(self, health):
        if self.health < 0:
            raise NoHealth('Вы умираете')

    def mood(self, mood):
        if self.mood < 0:
            raise NoMood('Вы впали в депрессию')

    def money(self, money):
        if self.money < 0:
            raise NoMoney('Вы банкрот')
    def change_state(self, health, mood, money):
        self.money = self.money + money
        self.health = self.health + health
        self.mood = self.mood + mood

    def action(self, action):
        self.money = self.money + action.money
        self.health = self.health + action.health
        self.mood = self.mood + action.mood