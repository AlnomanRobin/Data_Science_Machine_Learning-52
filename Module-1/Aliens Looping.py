X = ["glazed", "chocolate", "sprinkle", "Nut"]
for Y in X: # Loop through each element in the list X
    print(Y) #

print("\n")

angle = 0
while angle <=90:
    print(angle)
    angle = angle + 30

R = 10
while R > 0:
    print(R)
    R = R - 1


print("\nDonut menu:")
donuts = ["glazed", "chocolate", "sprinkle", "Nut"]
for number, donut in enumerate(donuts, start=1):
    print(f"{number}. {donut} donut")

print("\nNumbers from 1 to 100:")   # Print numbers from 1 to 100
for number in range(1, 101):
    print(number)

print("\nEven numbers from 0 to 100:")
for number in range(0, 101):  # 0 থেকে শুরু করে 100 পর্যন্ত যাবে
    if number % 2 == 0:  # 2 দিয়ে ভাগ করলে ভাগশেষ 0 হলে সংখ্যাটি জোড়
        print(number)


print("\nOdd numbers from 0 to 100:")
for number in range(0, 101):  # 0 থেকে শুরু করে 100 পর্যন্ত যাবে
    if number % 2 != 0:  # 2 দিয়ে ভাগ করলে ভাগশেষ 0 না হলে সংখ্যাটি বিজোড়
        print(number)


initial = 3
while initial > 0:
    print(initial)
    value = 0
    while value < 3:
        print(value)
        value = value + 1
    initial = initial - 1

