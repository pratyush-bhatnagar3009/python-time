import random
number = random.randint(1,9)
chances = 0
print("number guessing game you have three chances")
print("All the best")
while (chances<3):
    answer = int(input("enter your choice"))
    if(answer==number):
        print("you are great you win!")
        break
    else:
        chances=chances+1
        print("Try again")