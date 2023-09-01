import random
import time

random_number = random.randint(1, 1000)
guess_limit = 11
print("""***********************************

Welcome the game of Yaren :) :) :) :) :)
Let's get try to guess number between 1-1000:) :) :) :) :)
Good luck ;) ;) ;) ;) ;) ;)

***********************************""")
while True:
    guess = int(input("enter your guess:"))
    if guess < random_number:
        print("Your guess is being checked. Please wait......")
        time.sleep(2)
        print("HINT: Enter a larger number ;) ;) ;)")
        guess_limit -= 1
    elif guess > random_number:
        print("Your guess is being checked. Please wait......")
        time.sleep(2)
        print("HİNT: Enter a smaller number ;) ;) ;)")
        guess_limit -= 1
    else:
        print("Congratulations !!!!! :) :) :) :)")
        break
    if guess_limit == 0:
        print("You have run out of guesses :( :( :(")
        print("random number is", random_number)
        break
