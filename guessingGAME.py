import random

print("number guessing game")

number = random.randint(1, 9)

chances = 0

print("guess any number between 1 and 9:")

while chances < 3:
    guess = int(input("Enter your guess - "))

    if guess == number:
        print("YOU WON")
        break

    elif guess < number:
        print("YOU LOST")

    else:
        print("YOU LOST", guess)

    chances += 1

if not chances < 3:
    print("YOU LOST", number)
