# essentially just an array

foo = ["all", "this", "stuff", "extra whitespace   "]
names = ["dallas sherman", "charmaine sherman"]

print(foo[1])
print(foo)
print(foo[0].title())
print(foo[3])
print(foo[3].title())


print(names[0].title())
print(names[1].title())

names[0] = "blubber"

print(names)

# add to end of list(array)
names.append("dallas sherman")

# insert to position in list (this overwrites the existing value)
names.insert(0, "scotty g")


for name in names:
    print(f"Hello {name.title()}")
    print("DONE")


del names[1]

print(names)

# take off the last item
popped_dallas = names.pop()

print(f"{popped_dallas.title()} got popped.")
print(names)

# pop from a position in the list
popped_char = names.pop(1)
print(f"{popped_char.title()} also got popped")

names.append("hurdur")
print(names)

names.remove("hurdur")

print(names)

new_list = [1, 10, 2, 40, 3, 60, 4, 6, 9]
print(new_list)

print(f"\n\ncan also sort them temporarily:")
print(sorted(new_list))
print("\nHere's the original:")
print(new_list)

new_list.sort()
print(f"\n\n")
print(new_list)

# reverse list w/ .reverse()

print(len(new_list))
