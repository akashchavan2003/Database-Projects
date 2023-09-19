import random

print("enter any char value")
a = str(input())
ran = random.randint(65, 70)
temp = chr(ran)
x = ran
print("the correct is ", temp)
if a == temp or a == str(x - 1) or a == str(x + 1):

    print("you guess right")
else:
    print("try again")
