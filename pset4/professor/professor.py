import random

def main():
    level = get_level()
    score = game(level)
    print(f"Score: {score}")

def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if 1 <= level <= 3:
                return level
            else:
                print("Please enter a valid level (1, 2, or 3).")
        except ValueError:
            print("Invalid input. Please enter a number.")

def game(level):
    game_round = 1
    score = 0
    while game_round <= 10:
        x, y = generate_integer(level)
        user_respond = round_question(x, y)
        if user_respond:
            score += 1
        game_round += 1
    return score

def generate_integer(level):
    if level == 1:
        x = random.randint(0, 9)
        y = random.randint(0, 9)
    elif level == 2:
        x = random.randint(10, 99)
        y = random.randint(10, 99)
    elif level == 3:
        x = random.randint(100, 999)
        y = random.randint(100, 999)
    return x, y

def round_question(x, y):
    answer = x + y
    tries = 1
    while tries <= 3:
        try:
            user = int(input(f"{x} + {y} = "))
            if user == answer:
                return True
            else:
                print("EEE")
                tries += 1
        except ValueError:
            print("EEE")
            tries += 1
    print(f"{x} + {y} = {x + y}")
    return False

if __name__ == "__main__":
    main()
