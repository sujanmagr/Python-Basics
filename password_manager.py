#Password manager that store the username and password
from cryptography.fernet import Fernet


def load_key():
    file=open('key.key', 'rb')
    key=file.read()
    file.close()
    return key

master_pwd=input("What is the master password?: ")

key=load_key()+master_pwd.encode()
fer = Fernet(key)

'''def write_key():
    key=Fernet.generate_key()
    with open("key.key", 'wb') as key_file:
        key_file.write(key)
write_key()
'''
def view():
    with open("password.txt", 'r') as f:
        for line in f.readlines():
            data=line.rstrip()
            user, passw =data.split("!")
            print("user: ", user, "\npassword: ", fer.decrypt(passw.encode()).decode())

def add():
    name=input("Account Name: ")
    pwd=input("Password: ")
    
    with open('password.txt', 'a')as f:
        f.write(name+ "! "+fer.encrypt(pwd.encode()).decode()+ "\n") 
        


while True:
    mode=input("Would you like to add a new passwprd or view existing ones (view, add): ").lower()
    if mode=="q":
        break

    elif mode=="view":
        view()

    elif mode=="add":
        add()

    else:
        print("Invalid Option!")
