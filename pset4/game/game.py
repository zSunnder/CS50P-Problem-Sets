import random

# Ask for the level
while True:
    try:
        level = int(input("Level: "))
        if level >= 1:
            break
        else:
            continue
    except ValueError:
        continue

# Generate a random number
number = random.randint(1, level)

while True:
    # Ask for the user's guess
    try:
        guess = int(input("Guess: "))
    except ValueError:
        print("Please enter a valid number.")
        continue

    # Check if the guess is correct
    if guess == number:
        print("Just right!")
        break
    elif guess > number:
        print("Too large!")
    else:
        print("Too small!")






