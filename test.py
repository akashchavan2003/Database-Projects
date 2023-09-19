import random

print("enter first player name")
a = str(input())
print("enter second player name")
b = str(input())
while True:
    random.seed()
    input()
    temp = random.randint(1, 6)
    print("you get", temp)
    input()
    temp2 = random.randint(1, 6)
    print("you get", temp2)
    if temp == 6:

            print("player",a)
            input()
            temp3 = random.randint(1, 6)
            print("in double chance you get", temp3)
            if temp3 == 6:
                print("YOU WIN....")
            break
    if temp2 == 6:
        print("player", b)
        input()
        temp4 = random.randint(1, 6)
        print("in double chance you get", temp4)
        if temp4 == 6:
            print("YOU WIN....")
    break
print("game over")
