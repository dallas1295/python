prompt = "\nTell me something and I'll repeat it back to you,"
prompt += "\nEnter 'quit' to end the program.\n"

# message = ""
# while message != "quit":
#     message = input(prompt)
#     print(message)

active = True
while active:
    message = input(prompt)

    if message == "quit" or "exit":
        active = False
    else:
        print(message)
