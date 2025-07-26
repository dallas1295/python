with open("input/day2.txt") as input:
    dimensions = input.read().splitlines()


# part 1
total_needed = 0

for dim in dimensions:
    l, w, h = map(int, dim.split("x"))
    surface_area = 2 * l * w + 2 * w * h + 2 * h * l
    smallest_side = min(l * w, w * h, h * l)

    total_needed = total_needed + surface_area + smallest_side


print("part 1 is", total_needed)

# part 2
total_ribbon = 0

for dim in dimensions:
    l, w, h = map(int, dim.split("x"))

    dims = [l, w, h]
    dims.sort()
    smallest_perimeter = 2 * (dims[0] + dims[1])

    bow_ribbon = l * w * h

    total_ribbon = total_ribbon + smallest_perimeter + bow_ribbon

print("part 2 is", total_ribbon)
