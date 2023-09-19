import random

player = 1
question = 1
ls = ["+", "-", "*", "**", "<", ">", "!=", "=="]
pla = 0
count1 = 0
pla2 = 0
count2 = 0
user_an = 0
while True:
    random.seed()
    a = random.randint(1, 6)
    b = random.randint(1, 6)
    ch = random.choice(ls)
    ex = f"{a} {ch} {b}"
    an = eval(ex)

    if player == 1:
        print("answer the following questions for player", player)
        print("question no.", question, ".", a, ch, b)
        q1 = input()
        print("answer is", an)
        count1 += 1
        question += 1
        if q1.lower() == "true":
            user_an = True
        if q1.lower() == "false":
            user_an = False
        if user_an == an:
            pla += 1
        else:
            if q1 == str(an):
                pla += 1

        if count1 >= 5:
            player = 2
            question = 1
            print("you have taken your 5 questions")
    if player == 2:
        print()
        print("answer the following questions for player", 2)
        print("question no.", question, "=", a, ch, b)
        q1 = input()
        print("answer is", an)
        count2 += 1
        question += 1
        if q1.lower() == "true":
            user_an = True
        if q1.lower() == "false":
            user_an = False
        if user_an == an:
            pla2 += 1
        else:
            if q1 == str(an):
                pla2 += 1
        if count2 >= 5:
            print("you have taken your 5 questions")
            break
print("player 1 has correct question is", pla, "out of 5")
print("player 2 has correct question is", pla2, "out of 5")
if pla > pla2:
    print("so, player 1 wins....")
if pla2 > pla:
    print("so , player 2 wins...")
else:
    print("so, match tie....")
print("game over press ENTER to exit")
input()
