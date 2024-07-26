import random

def guess_MyNumber():
    # Let's determine the number that the computer randomly keeps
    number_toGuess = random.randint(1,100)
    guess = None 
    attempts = 0

    print("I kept a number between 1 and 100. See if you can guess it?")

    while guess != number_toGuess:
        #Let's ask the user for a prediction
        guess= int(input("Your Estimate: "))
        attempts += 1

        if guess < number_toGuess:
            print("Guess a bigger number!")
        elif guess > number_toGuess:
            print("Guess a smaller number!")

    print(f"Congratulations! You found {number_toGuess} in {attempts} attempts.")

#Let's start the game 
guess_MyNumber()
