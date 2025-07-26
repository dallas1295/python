import os


def file_create():
    base_path = os.path.join(os.path.expanduser("~"), "projects", "python")
    user_input = input("Enter a file name: ")
    filename = f"{user_input}.txt"
    full_path = os.path.join(base_path, filename)

    try:
        os.makedirs(base_path, exist_ok=True)
        print(f"Directory '{base_path}' exists!")

        with open(full_path, "w") as file:
            file.write("Hello\n")
            file.write("This is a test to ensure this works!")
            print(f"Successfully written to {filename}")
    except PermissionError:
        print(f"Access Permission Denied")
    except OSError as e:
        print(f"An operating system error occurred: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    file_create()
