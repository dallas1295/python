class User:
    """An exmaple of a user for a DB"""

    def __init__(self, username, first_name, last_name):
        """basic model"""
        self.username = username
        self.first_name = first_name.title()
        self.last_name = last_name.title()

    def login(self):
        """Basic prompt"""
        print(f"{self.username} has been logged in")
        print(f"Welcome {self.first_name} {self.last_name}.")

    def logout(self):
        """Another basic prompt"""
        print(f"{self.username} has been logged out")
        print(f"Goodbye {self.first_name} {self.last_name}!")


me = User("dallas1295", "dallas", "sherman")
another = User("blubby", "blub", "blubber")

another.login()
me.login()

me.logout()
another.logout()
