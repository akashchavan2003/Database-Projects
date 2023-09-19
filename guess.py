import random

player = 1
flag = False
num = int(input("Enter a player of numbers: "))

while True:
    print("Enter a roll a dice for player", player)
    input()
    roll = random.randint(1, 6)
    print("you guessed", roll)
    if num != player:
        player += 1
    elif player == num:
        player = 1
    if roll == 6 and flag == False:
        flag = True
        continue

    elif roll == 6 and flag == True:
        print("player", player, "you win...")
        break
    else:
        flag = False

    if num != player:
        player += 1
    elif player == num:
        player = 1
