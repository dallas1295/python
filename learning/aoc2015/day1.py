with open("input/day1.txt") as input:
    movement = input.read()

# part 1
floor = 0
for move in movement:
    if move == "(":
        floor += 1
    elif move == ")":
        floor -= 1

print("part 1:", floor)

# part 2
floor = 0
instructions = 0

for move in movement:
    if move == "(":
        floor += 1
        instructions += 1
    elif move == ")":
        floor -= 1
        instructions += 1

        if floor == -1:
            print(instructions)
            break
