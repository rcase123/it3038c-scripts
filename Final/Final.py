
from cryptography.fernet import Fernet


''' This code is used to create the key file used with
encryption, only used once is why its removed.

def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)


write_key()'''




'''This is opening that key file'''
def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key





'''Creating variables for the functions'''

key = load_key() 

fer = Fernet(key)


'''This is creating the function view by opening our txt file containing the encrypted passwords and decrypting them'''


def view():
    with open('password.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, password3 = data.split("|")
            print("User:", user, "| Password:",  fer.decrypt(password3.encode()).decode())

'''This is the process of adding new screen names and passwords to the encrypting file, and also creating the file if it's not there'''
 
def add():
    name = input('Screen Name: ')
    password2 = input('Password: ')
    with open('password.txt', 'a') as f:
        f.write(name + '|' + fer.encrypt(password2.encode()).decode() + "\n")

'''This is the process of checking the master password and bridging the multiple functions together'''

while True:
    password = input('Enter a Master Password: ')
    if password == 'rob':
        mode = input("There are three options. Would you like to add a password, view them, or close the program? Type (view, add, or quit) and Press Enter")
    if mode =="quit":
        break
    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid code. ")
        continue