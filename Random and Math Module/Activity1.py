import random

playing = True 
number = str(random.randint(1, 10))

print("I will generate a number from 1 to 10 , and you have to guess the number one at a time.")

print("THE GAME ENDS WHEN YOU GET 1 HERO!!")

while playing:
    guess = input("Give me your best guess! \n")
    if number == guess:
        print("YOU HAVE WON THE GAME!!")
        print("The number was indeed", number)
        break
    else:
        print("WRONG GUESS!! TRY AGAIN!!")