import random

temp = 0
print("enter your name")
a = str(input())
print("enter your name")
b = str(input())
while True:
    print(f"{a}, press enter to roll a dice")
    input()
    roll1 = random.randint(1, 6)
    print("you rolled", roll1)
    print(f"{b},press enter to roll a dice")
    input()
    roll2 = random.randint(1, 6)
    print("you rolled", roll2)

    if roll1 == 6:
        print(f"{a}get double chance to roll")
        input()
        roll3=random.randint(1,6)
        if roll3==6:
            print("you win")
        else:

            break
     if

