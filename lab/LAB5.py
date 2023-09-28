import random
number = random.randint(1, 10)
guesses = int(input("Enter a number between 1 and 10: "))
while True:
    if guesses < number:
        print ("Dang, too low")
        guesses = int(input("Enter a number between 1 and 10: "))
    elif guesses > number:
        print ("Dang, too high")
        guesses = int(input("Enter a number between 1 and 10: "))
    else:
        print ("You got it! Great job!!!")
        break