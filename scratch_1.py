import random

j = 0
i = 0
k = 0
number1 = 0
number2 = 0
while True:

    random.seed()
    number1 = random.randint(1, 10)
    number2 = random.randint(1, 10)

    i += 1
    j += number1
    k += number2

    if number1 == number2:
        print("the numbers are now the same...")
        print("number of time loop are run is:", i)
        print("the addition of random number of first", j)
        print("the addition of random number of second  is", k)
        print("the same value is :", number1)

        break
