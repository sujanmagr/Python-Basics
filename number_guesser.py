import random

top_number=input("type a number: ")

if top_number.isdigit():
    top_number=int(top_number)

    if top_number<=0:
        print("enter number larger than 0")
        quit()

else:
    print("enter a number please!")

random_number=random.randint(0, top_number)
guess=0
while True:
    guess+=1
    user_guess=input("guess the number: ")
    if user_guess.isdigit():
        user_guess=int(top_number)

    else:
        print("enter a number please!")
        continue

    if user_guess==random_number:
        print("wow, correct guess")
        break

   
    elif user_guess > random_number:
        print("you are above the number. Try again!")

    else:
        print("you are below the number. Try again!")

print("you got it in", guess, "guesses")