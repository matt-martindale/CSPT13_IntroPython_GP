# lets make a guessing game
# set a value
# take in some input from a player
# check it against a value
# if they are the same print player wins
# if they are different print guess again
# and loop

number = 45
is_playing = True

while is_playing:
    guessed_number = int(input("Guess the number I'm thinking of >>> ")) # READ

    #EVAL
    if number == guessed_number:
        print("You guessed right!!") #PRINT
        is_playing = False
    else:
        print("Wrong, guess again")