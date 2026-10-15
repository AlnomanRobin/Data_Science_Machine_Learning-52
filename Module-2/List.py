snacks = ["Chips", "Soda", "Cake"]
print("Snacks: ", snacks)

snacks.append("Cookies")
print("After adding cookies: ", snacks)

snacks.remove("Soda")
print("Soda was too fizzy, Removed: ", snacks)

snacks.sort()
print("Snacks in alphabetical order:", snacks)

print("\n")

snacks = ["Chips", "Cake", "Soda", "Pizza"]
print("First snack: ", snacks[0])
print(len(snacks))
print("Last snack: ", snacks[-1])

snacks[2] = "Juice"
print("After replacement: ", snacks)

snacks.insert(1, "Cookies")
print("After inserting Cookies: ", snacks)

del snacks[4]
print("After deleting Pizza: ", snacks)

last_snack = snacks.pop()
print("Popped item: ", last_snack)
print("Remaining item: ", snacks)

snacks.clear()
print("After clearing: ", snacks)


snacks = ["Chips", "Cake", "Soda", "Pizza"]
print(snacks[1:3])

index_list = [0, 2, 3]
for i in index_list:
    print(snacks[i])


party_bags = [
    ["Chips", "Cookies"],
    ["Cake", "Juice"],
    ["Soda", "Pizza"]
]

for bag in party_bags:
    for item in bag:
        print("Bag has: ", item)


party_bags = [
    ["Chips", "Cookies"],
    ["Cake", "Juice"],
    ["Soda", "Pizza"]
]

for bag in party_bags:
    for item in bag:
        print("Bag has: ", item)

print("\n")


party_bags = [
    ["Chips", "Cookies"],
    ["Cake", "Juice"],
    ["Soda", "Pizza"]
]

for bag in party_bags:
    for item in bag:
        print("Bag has: ", item)


for index, bag in enumerate(party_bags):
    print(f"Bag {index}: ", bag)
    for item in bag:
        print("Bag has: ", item)
