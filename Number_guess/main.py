import random
num = random.randint(0,100)

count=0
while count <=5:
    count+=1
    userval = int(input("enter number"))

    if userval == num:
        print("correct guess")
        break
    elif userval<num:
        print("guessed small")
    elif userval>num:
        print("guessed high")
if count>5:
    print("better luck next time")

    