from person import Person
from action import Action
from action import Work
from action import Rest



import random

human = Person(name = 'Тарас', money = 0, mood = 100, health = 100)
human1 = Person(name = 'Олег', money = 0, mood = 90, health = 100)
human2 = Person(name = 'Костя', money = 0, mood = 100, health = 80)

print(human)
print(human1)
print(human2)

human.change_state(
        money = random.randint(50, 100),
        mood = random.randint(-20, -10),
        health = random.randint(-10, -5)
    )
human1.change_state(
        money = random.randint(50, 100),
        mood = random.randint(-20, -10),
        health = random.randint(-10, -5)
    )
human2.change_state(
        money = random.randint(50, 100),
        mood = random.randint(-20, -10),
        health = random.randint(-10, -5)
    )

print(human)
print(human1)
print(human2)

go_to_factory = Work(name = 'Пойти на завод', money = 50, mood = -10, health = -3)
go_to_park = Rest(name = 'Сходить в парк', money = 0, mood = 15, health = 3)
go_to_hospital = Action(name = 'Пойти в больницу', money = -20, mood = -5, health = 20)


print(type(go_to_hospital))