import random

affection = 0
afflevel = ("classmates", "friends", "lover", "wife", "yandere")
level = 0

while affection < 110:
    value = random.randint(1, 16)
    affection += value
    level = affection // 25
    print("Affection is increased by", value, "Affection is now", affection)
    print("Your affection level is now", afflevel[level])

print()
print("Have fun!~")
