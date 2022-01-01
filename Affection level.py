from random import *

affection = 0
afflevel = ("classmates", "friends", "lover", "wife", "yandere")
level = 0

while (affection < 110):
    value = randint(1, 16)
    affection += value
    level = affection // 25
    print("Affication is increased by", value, "Affection is now", affection)
    print("Your affection level is now", afflevel[level])

print()
print("Have fun!~")
