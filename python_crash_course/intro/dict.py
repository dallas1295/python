test_dict = {"foo": "bar", "one": "1", "two": "2"}

print(test_dict)

first = test_dict["foo"]

print(f"this is foo {first}")

my_languages = {
    "python": "beginner",
    "go": "beginner",
    "C": "N/A",
    "rust": "beginner",
    "Typescript/Javascript": "intermediate,",
}

# if i try to do .get() without a corresponding key it will return None
point_val = my_languages.get("language")

print(point_val)

user_0 = {
    "username": "tilteasy",
    "first": "dallas",
    "last": "sherman",
}

for key, value in user_0.items():
    print(f"\nKey: {key}")
    print(f"Value: {value}\n")


my_languages = {
    "python": "beginner",
    "go": "beginner",
    "C": "N/A",
    "rust": "beginner",
    "typescript/javascript": "intermediate,",
}

for language, level in my_languages.items():
    print(language.title())
    print(
        f"{language.title()} is one of the languages I can program in. I'm a {level} coder at it\n"
    )
