import hashlib

with open("input/day4.txt") as input:
    data = input.read().strip()

    # part 1
index = 1
while True:
    key = data + str(index)
    digest = hashlib.md5(key.encode("ascii")).hexdigest()
    if digest[:5] == "00000":
        break
    index += 1

print(index)

# part 2
index = 1
while True:
    key = data + str(index)
    digest = hashlib.md5(key.encode("ascii")).hexdigest()
    if digest[:6] == "000000":
        break
    index += 1

print(index)
