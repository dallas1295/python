from random import randint


def guessing_game():
    input_str = None

    try:
        random_int = randint(0, 10)
        input_str = input("Enter a number between 1 and 10: ")

        guess = int(input_str)
        print(f"you chose: {guess}")

        print(f"The computer chose: {random_int}")
        if guess == random_int:
            print(
                f"You win\nthe random number {random_int} is the same as yours {guess}"
            )
        elif guess < random_int:
            print("You Lose!\nYour guess was too low")
        elif guess > random_int:
            print("You Lose!\nYour guess was too high")

    except ValueError:
        print("you need to use a number!")


if __name__ == "__main__":
    guessing_game()
