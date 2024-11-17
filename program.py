import numpy as py
secret_no=int(py.random.randint(1,11))

def guess_number():
    counter = 1
    while counter <= 6:
        guess_no=int(input("Enter a guess between 1 to 10:"))
        if guess_no==secret_no:
            print("You won")
            break
        elif (guess_no >= secret_no):
            print("your guess is too long!")
        else:
            print("Try again")
        counter = counter+1
        if counter ==6:
            print("your chance finish game over!")
            break    
guess_number()