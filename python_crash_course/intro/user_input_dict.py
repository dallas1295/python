responses = {}

active = True

while active:
    # Prompt for info
    name = input("\nWhat's your name? ")
    response = input("What do you like to do? ")

    # Store
    responses[name] = response

    # Find out if the user wants to repeat
    repeat = input("Would you like to add another hobby? (y/n) ")

    if repeat == "n":
        active = False

    print("\n--- Your Hobbies ---")
    for name, response in responses.items():
        print(f"{name} likes to {response}.")
