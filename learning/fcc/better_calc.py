first = float(input("Enter first number: "))
second = float(input("Enter second number: "))
op = input("Enter operand: ")

if op == "+":
    print(first + second)
elif op == "-":
    print(first - second)
elif op == "*":
    print(first * second)
elif op == "/":
    print(first / second)
else:
    print("Invalid operand")
