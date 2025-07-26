class Dog:
    """A simple model of a dog"""

    # self is defined first in the method and it must come first.
    # in order for the instnace of Dog to work it MUST have a self declaration, and the method automatically passes self
    ### the reason why self is important is because it is the reference to the the instance it(self).
    def __init__(self, name, age):
        """Init the name and age attributes"""
        self.name = name
        self.age = age

    def sit(self):
        """Simulate a dog sittings in response to command"""
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        """Simulate rolling over in response to command"""
        print(f"{self.name} rolled over!")


his_dog = Dog("Willie", 6)
my_dog = Dog("Thor", 11)

print(f"My dog's name is {my_dog.name}")
print(f"My dog is {my_dog.age} years old")

my_dog.sit()
my_dog.roll_over()

print(f"His dog's name is {his_dog.name}")
print(f"His dog's age is {his_dog.age}")
his_dog.sit()
