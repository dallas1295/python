with open("input/day3.txt") as input:
    directions = input.read()

x, y = 0, 0

# part 1
visited = {(x, y)}

for dir in directions:
    if dir == "^":
        y += 1
    elif dir == "v":
        y -= 1
    elif dir == ">":
        x += 1
    elif dir == "<":
        x -= 1
    visited.add((x, y))

print("Part 1", len(visited))

# part 2
sx, sy = 0, 0
rx, ry = 0, 0

visited = {(0, 0)}

for index, direction in enumerate(directions):
    if index % 2 == 0:
        if direction == "^":
            sy += 1
        elif direction == "v":
            sy -= 1
        elif direction == ">":
            sx += 1
        elif direction == "<":
            sx -= 1
        visited.add((sx, sy))
    else:
        if direction == "^":
            ry += 1
        elif direction == "v":
            ry -= 1
        elif direction == ">":
            rx += 1
        elif direction == "<":
            rx -= 1
        visited.add((rx, ry))

print("Part 2", len(visited))

