import random

SEPARATOR = "=" * 80

def welcome():
    print("Hi there! Welcome to the Bulls & Cows game!")
    print(SEPARATOR)
    print("I've generated a random 4 digit number for you. Can you guess it?\n"
          "Let's play the game!")
    print(SEPARATOR)

    return (welcome)


random_number = []


def number_generator():
    while len(random_number) != 4:
        random_number.append(random.randrange(0, 10))
        if len(random_number) == 4 and len(set(random_number)) < 4:
            random_number.clear()

    return (random_number)


bulls = 0
cows = 0
tries = 0
remaining_tries = 15


def game():
    global bulls, cows, tries, remaining_tries

    while bulls != 4 and remaining_tries > 0:

        while True:
            try:
                players_input = input("Please enter your guess (must be a 4 digit number): ")
                players_guess = [int(number) for number in str(players_input)]
            except ValueError:
                print("Numbers only please! Try again.")
                print(SEPARATOR)
                continue

            if len(players_guess) != 4 or len(set(players_guess)) < 4 or players_guess[0] == 0:
                print("You must enter a 4 digit number! Each number must be unique.")
                print(SEPARATOR)
                continue

            tries += 1
            remaining_tries -= 1

            if remaining_tries == 0:
                print(SEPARATOR)
                print("GAME OVER! Better luck next time!")
                game_over = "".join(map(str, random_number))
                print(f"The secret number was: {game_over}")
                continue

            for index, value in enumerate(players_guess):
                for position, num in enumerate(random_number):
                    if index == position and value == num:
                        bulls += 1

                    elif index != position and value == num:
                        cows += 1

            print(f"Bulls: {bulls}")
            print(f"Cows: {cows}")
            print(f"Remaining tries: {remaining_tries}")
            print(SEPARATOR)

            if remaining_tries == 0:
                print("GAME OVER! Better luck next time!")
                game_over = "".join(map(str, random_number))
                print(f"The secret number was: {game_over}")

            elif bulls != 4:
                bulls = 0
                cows = 0

            else:
                bulls = 4
                cows = 0

                if tries < 8:
                    print(f"Congratulations, you WON!!! Number of tries: {tries} out of {remaining_tries}")

                elif tries >= 8 and tries < 15:
                    print(f"You WON! But it could be better! Number of tries: {tries} out of {remaining_tries}")

welcome()
number_generator()
game()
