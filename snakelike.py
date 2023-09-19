import random

tot1 = 0
tot2 = 0
print("Enter player 1's name:")
a = str(input())

print("Enter player 2's name:")
b = str(input())

while True:
    print(" press enter to roll a dice", a)
    input()
    roll1 = random.randint(1, 6)
    print(a, " rolled:", roll1)
    if tot1 + roll1 <= 15:
        tot1 += roll1
    print(a, 'your total now is', tot1)
    if tot1 == 15:
        print("you win")
        break

    print(" press enter to roll a dice", b)
    input()
    roll2 = random.randint(1, 6)
    print(b, " rolled:", roll2)

    if tot2 + roll2 <= 15:
        tot2 += roll2
    print(b, "your total now is", tot2)
    if tot2 == 15:
        print("you win..")
        break
print("to exit press enter")
input()
