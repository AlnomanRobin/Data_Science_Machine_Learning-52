guest = {
    "name": "Sunny",
    "age": 25,
    "favourite_snack": "Cake"
}
print("Guest details: ", guest)
print("Guest name: ", guest["name"])
print("favourite snack: ", guest["favourite_snack"])

guest["favourite_snack"] = "Chips" # Update the favourite snack
print("Updated snack", guest)

guest["Phone"] = "123-455-895" # Add a phone number
print("Added phone number: ", guest)

del guest["age"] # Remove the age
print("After removing age: ", guest)

guest.pop("Phone") # Remove the phone number
print("After removing phone number: ", guest)

guest.clear() # Clear the dictionary
print("After clearing: ", guest)
print("\n")

guest = {
    "name": "Sunny",
    "age": 25,
    "favourite_snack": "Cake"
}
for key, value in guest.items():
    print(f"{key}: {value}")


party_guests = {
    "guest1": {"name": "Sunny", "snack": "Chips"},
    "guest2": {"name": "Imran", "snack": "Cake"}
}

print(party_guests["guest2"]["name"])

for guest_id, details in party_guests.items():
    print(guest_id, "->", details["name"], "likes", details["snack"])

