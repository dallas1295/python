def greet_user(name):
    """Display a simple greeting"""
    print(f"Hello, {name.title()}!")


user_name = input("What's your name? ")
if not user_name.strip():
    user_name = "User"

greet_user(user_name)
