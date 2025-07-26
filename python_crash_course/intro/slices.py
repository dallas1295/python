players = ["charles", "martina", "michael", "florence", "eli"]

# print(players[0:3])
# or
print(players[:3])


# can also pick where to start
print(players[2:])
# or be specific
print(players[2:4])


for player in players[:3]:
    print(player.title())
