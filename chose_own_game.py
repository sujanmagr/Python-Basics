name=input("Enter your name: ")
print(f"Welcome {name} to this adventure game!")


answer=input("you are on a dirt road, it has come to an end and you can go left or right. which way would you to go? ").lower()

if answer=="left":
    answer=input("You come to a river. Now you can either walk around or swim in it. Which option would you chose?").lower()

    if answer=="swim":
        print("Opps there was an anoconda you failed... :(")


    elif answer=="walk":
        print("Yeah you are walking for a while wanna swim or keep walking.")
    else:
        print("Invalid Option chose one please!")



elif answer=="right":
    answer=input("oh! there is a bridge do you wanna cross it or wanna go back?").lower()

    if answer=="cross":
        answer=input("you have met a stranger. Do you wann talk to him?").lower()

        if answer=="yes":
            print("Wow he gave you a gold. You win!")
        
        elif answer=="no":
            print("he was the man to make you win. you lost!")

        else:
            print("Invalid option.")
    elif answer=="back":
        print("Your are quiting the game. You lost!")
    
    else:
        print("Invalid option!")



else:
    print("Invalid option chose one please!")