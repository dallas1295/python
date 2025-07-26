with open("input/day5.txt") as input:
    data = [line.strip() for line in input.readlines()]


vowels = "aeiou"
bad_strings = ["ab", "cd", "pq", "xy"]
count = 0
for word in data:
    if sum(c in vowels for c in word) < 3:
        continue

    twice = False
    for i, c in enumerate(word[:-1]):
        if word[i + 1] == c:
            twice = True
            break
    if not twice:
        continue

    is_bad = any(bad in word for bad in bad_strings)
    if is_bad:
        continue

    count += 1

print(count)

## part 2

for word in data:
    count = 0
    is_twice = False
    for index in range(len(word) - 1):
        ab = word[index : index + 2]
        for index_two in range(index + 2, len(word) - 1):
            cd = word[index_two : index_two + 2]
            if ab == cd:
                is_twice = True
                break
        if is_twice:
            break

    repeating = False
    for index in range(len(word) - 2):
        if word[index] == word[index + 2]:
            repeating = True
            break
    if repeating:
        break

    count += 1

print(count)
