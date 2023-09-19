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
    tot1 += roll1
    print('your total now is', tot1)
    if tot1>21:
        tot1=
    if tot1 == 20:
        print("you win")
        break
    print(" press enter to roll a dice", b)
    input()
    roll2 = random.randint(1, 6)
    print(b, " rolled:", roll2)
    tot2 += roll2
    print("your total now is", tot2)

    if tot2 == 20:
        print("you win..")
        break
