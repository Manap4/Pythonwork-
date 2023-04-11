import random

while True:
    try:
        level = int(input("Please enter a level (positive integer): "))
        if level > 0:
            break
        else:
            print("Invalid input, please try again.")
    except ValueError:
        print("Invalid input, please try again.")

secret_number = random.randint(1, level)

while True:
    try:
        guess = int(input("Please guess the number: "))
        if guess <= 0:
            print("Invalid input, please try again.")
            continue
        if guess < secret_number:
            print("Too small!")
        elif guess > secret_number:
            print("Too large!")
        else:
            print("Just right!")
            break
    except ValueError:
        print("Invalid input, please try again.")