# A tuple is ordered and immutable, so its values cannot be changed directly.
my_tuple = ("apple", "banana", "cherry")

print(my_tuple)
print(len(my_tuple))  # Find the number of items in the tuple.
print(my_tuple[0])  # Access the first item using its index.
print(my_tuple[-1])  # Access the last item using a negative index.
print(my_tuple[1:3])  # Select items from index 1 up to, but not including, index 3.
print("banana" in my_tuple)  # Check whether an item exists in the tuple.
print("\n")

# Convert the tuple to a list when a value needs to be changed.
fruits_list = list(my_tuple)
print(fruits_list)
fruits_list[1] = "kiwi"  # Lists are mutable, so their items can be updated.
print(fruits_list)
print(tuple(fruits_list))  # Convert the modified list back into a tuple.
print("\n")

# Extended unpacking assigns the first two items and collects the rest in a list.
fruits = ("apple", "banana", "cherry", "tomato")
(green, yellow, *red) = fruits
print(green)
print(yellow)
print(red)
print("\n")

# The + operator combines two tuples into a new tuple.
table1 = (1, 2, 3, 4, 5)
table2 = ("a", "b", "c")
table3 = table1 + table2
print(table3)
