import random

secret_number = random.randint(1,100)

print("----Guess the number----")
guess = None
attempt = 0

while secret_number != guess:
    try:   
        attempt=attempt+1
        guess=int(input("Your guess:"))

        if(secret_number<guess):
            print("Too high")
        elif (secret_number>guess):
            print("Too less")    
        else:
            print(f'You guess the right number in {attempt} attempt')
    except ValueError:
        print("enter valid value")
