print("welcome to my quiz!")


playing = input("Do you want to play? ")

if playing.lower()!="yes":
    print("thanks! \nquiting.....")
    quit()

print("Okey! Lets play.")
score=0
answer=input("What does CPU stands for? \n")

if answer.lower()=="central processing unit":
    print("wow. Thats correct.")
    score+=1

else: 
    print("Incorrect! Nice try BTW.")

answer=input("What does GPU stands for? \n")

if answer.lower()=="graphics processing unit":
    print("wow. Thats correct.")
    score+=1

else: 
    print("Incorrect! Nice try BTW.")


answer=input("What does RAM stands for? \n")

if answer.lower()=="random access memory":
    print("wow. Thats correct.")
    score+=1

else: 
    print("Incorrect! Nice try BTW.")

print("you got " + str(score) + " question correct!")