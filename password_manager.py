#Password manager that store the username and password

pwd=input("What is the master password?: ")
while True:
    mode=input("Would you like to add a new passwprd or view existing ones (view, add): ").lower()
    if mode=="q":
        break

    elif mode=="view":

    elif mode=="add":

    else:
        print("Invalid Option!")
