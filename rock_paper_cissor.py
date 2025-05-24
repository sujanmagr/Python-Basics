import random

user_win=0

computer_win=0

game=["rock", "paper", "scissor"]
while True:
    user_input=input("chose rock/ paper/ scissor or Q to quit: ").lower()
    if user_input=="q":
        break

    if user_input not in game:
        continue

    random_choice=random.choice(game)
    print("computer picked: ", random_choice)

    if user_input=="rock" and random_choice=="scissor":
        print("Congrats! you won.")
        user_win+=1
        continue

    elif user_input=="paper" and random_choice=="rock":
        print("Congrats! you won.")
        user_win+=1
        continue

    elif user_input=="scissor" and random_choice=="paper":
        print("Congrats! you won.")
        user_win+=1
        continue

    else:
        print("you lost!")
        computer_win+=1
        continue




print("you won: ", user_win, "times")
print("computer won: ", computer_win, "times")

print("GoodBye!")


