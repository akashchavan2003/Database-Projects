import random

player = 1
flag = False
count1 = 1
count2 = 1
count3 = 1
count = 4
position1 = 0
position2 = 0
position3 = 0
position4 = 0
ladders = [(2, 15), (18, 35), (48, 70), (55, 67), (65, 85), (80, 100)]
snakes = [(34, 20), (46, 25), (99, 13), (97, 72), (54, 20)]
check = 0
while True:
    # this blocks repeat upto over any one player gets 100
    print("Press enter to roll a dice for player", player)
    input()
    roll = random.randint(1, 6)
    print("player ", player, "rolled", roll)
    # this conditions checks for player 1 for checking it does exceed 100 to adding roll in it
    if player == 1:
        if position1 + roll <= 100:
            position1 += roll
            print("player ", player, "position is", position1)
        for x in ladders:
            if position1 == x[0]:
                print("you got a ladder from", x[0], "now you goes to", x[1])
                position1 = x[1]
                print("now your position is", position1)
        for y in snakes:
            if position1 == y[0]:
                print(f"Oh dear! You've encountered a snake at position {y[0]}. You will now descend to position {y[1]}")
                position1 = y[1]
                print("now your position is", position1)
    # this condition for player 2 for checking it does not exceeding 100 to adding roll in it
    if player == 2:
        if position2 + roll <= 100:
            position2 += roll
            print("player ", player, "position is", position2)
        for x in ladders:
            if position2 == x[0]:
                print("you got a ladder from", x[0], "now you goes to", x[1])
                position2 = x[1]
                print("now your position is", position2)
        for y in snakes:
            if position2 == y[0]:
                print(f"Oh dear! You've encountered a snake at position {y[0]}. You will now descend to position {y[1]}")
                position2 = y[1]
                print("now your position is", position2)
    if player == 3:
        if position3 + roll <= 100:
            position3 += roll
            print("player ", player, "position is", position3)
        for x in ladders:
            if position3 == x[0]:
                print("you got a ladder from", x[0], "now you goes to", x[1])
                position3 = x[1]
                print("now your position is", position3)
        for y in snakes:
            if position3 == y[0]:
                print(f"Oh dear! You've encountered a snake at position {y[0]}. You will now descend to position {y[1]}")
                position3 = y[1]
                print("now your position is", position3)
    if player == 4:
        if position4 + roll <= 100:
            position4 += roll
            print("player ", player, "position is", position4)
            for x in ladders:
                if position4 == x[0]:
                    print("you got a ladder from", x[0], "now you goes to", x[1])
                    position4 = x[1]
                    print("now your position is", position4)
            for y in snakes:
                if position4 == y[0]:
                    print(f"Oh dear! You've encountered a snake at position {y[0]}. You will now descend to position {y[1]}")
                    position4 = y[1]
                    print("now your position is", position4)
    # this block give repeat chance to every 6 roll

    if roll == 6 and player == 1:
        continue
    if roll == 6 and player == 2:
        continue
    if roll == 6 and player == 3:
        continue
    if roll == 6 and player == 4:
        continue
    # this checks if one of them get 100 it break the loop and exit from the loop
    if position1 == 100 or position2 == 100 or position3 == 100 or position4 == 100:
        if position1 == 100:
            print("Congratulation player 1 wins the match...........")
        elif position2 == 100:
            print("Congratulation player 2 wins the match...........")
        if position3 == 100:
            print("Congratulation player 3 wins the match...........")
        if position4 == 100:
            print("Congratulation player 4 wins the match...........")
        print("player 1 position is",position1)
        print("player 2 position is",position2)
        print("player 3 position is",position3)
        print("player 4 position is",position4)

        break
    # this changes the player all time upto loop breaks
    if player == 1:
        player = 2
    elif player == 2:
        player = 3
    elif player == 3:
        player = 4
    elif player == 4:
        player = 1
