import random

number=random.randint(1,10)

while True :

    enterednumber = int(input("Please guess a number between 1 and 10 :"))
    if enterednumber<number :
        print("Please increase your number")

    elif (enterednumber>number) :
        print("Please decrease your number")

    elif enterednumber==number :
        print("Your guess is correct the number is {}".format(number))
        break

