from random import randint


class Dice:
    def __init__(self, choice):
        """Setup the class for gameplay"""
        self.choice = choice

    def roll_dice(self):
        face = randint(1, 6)
        print(f"The computer has rolled a {face}.")
        print(f"you have rolled {self.choice}")

        if int(self.choice) == face:
            print("You win!")
        else:
            print("You lose")


if __name__ == "__main__":
    while True:
        user_input = input("Please input a number between 1 and 6: ")

        if user_input == "quit":
            break

        elif user_input < "1" or user_input > "6":
            print("please choose for a 6 sided die")

        else:
            Dice(user_input).roll_dice()
