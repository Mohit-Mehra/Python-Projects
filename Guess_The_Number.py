import random
number = random.randint(1,10)
for i in range(0,3):
    user = int(input("Guess a number :- "))
    if user == number:
        print("You Won!")
        print(f"You guessed the right it's {number}")
        break
if user!=number:
    print(f"You guess is incorrect the number is {number}")