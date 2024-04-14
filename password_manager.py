from cryptography.fernet import Fernet

def writekey():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)
def load():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key
master_password =input("What is the master password: ")
key = load()
fer = Fernet(key)

def view():
    with open("password.txt","r") as f:
        for line in f.readlines():
            data=line.rstrip()
            account,password=data.split(" ")
            print("User: "+account+" | password: "+fer.decrypt(password.encode()).decode())
def add():
    name = input("Account number: ")
    password = input("password: ")
    with open("password.txt","a") as f:
        f.write(name+" "+fer.encrypt(password.encode()).decode()+"\n")
while True:
    mode=input("Would you like to do add new password or view existing passowrd?(quit(q),add(a) or view(v)): ")
    if mode == "quit" or mode=="q":
        break
    elif mode=="view"or mode=="v":
        view()
    elif mode=="add"or mode=="a":
        add()