numbers = [1, 2, 42, 4531, 6432, 6, 3, 6, 8, 5, 9, 0]

print(min(numbers))
print(max(numbers))
print(sum(numbers))

for number in numbers:
    square = number**2
    print(square)
    cubed = number**3
    print(cubed)


numbers = [0]
# number = 0
# while number < 20:
#     number += 1
#     numbers.append(number)
#     print(number)
# this is same as this (less idiomatic)

for number in numbers:
    while number < 20

twenty_list = [value + 1 for value in range(0, 20)]
print(twenty_list)

# generating a cubes list
cubed = [value**3 for value in range(0, 11)]
print(cubed)
