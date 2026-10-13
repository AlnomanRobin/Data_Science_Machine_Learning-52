print("Wellcome to the Aliens Basics Operations module!")

distance_from_earth = 1000000  # in kilometers
fuel_efficiency = 0.5  # in kilometers per liter

fuel_needed= distance_from_earth * fuel_efficiency
print("fuel needed to reach the aliens: ", fuel_needed, "liters\n")

distance_to_home = float(input("Enter the distance to home in kilometers: "))
fuel_needed_to_home = 2 * distance_to_home  # in liters
print("fuel needed to reach home: ", fuel_needed_to_home, "liters\n")

chocolate = 3
sprinkle = 2
price_choco = 5
price_sprinkle = 6
total_cost = (chocolate * price_choco) + (sprinkle * price_sprinkle)
print("Total cost:", total_cost,"dollars")
tax = total_cost * 0.10
total_cost_with_tax = total_cost + tax
print("Total cost with tax:", total_cost_with_tax,"dollars\n")

total_slices = 8
aliens = 3
slices_per_alien = total_slices / aliens
print("Each alien gets:", slices_per_alien, "slices")
Full_slices = total_slices // aliens    #"//" used to find the quotient of the division
print("Full slices left:", Full_slices, "slices\n")

Leftover_slices = total_slices % aliens   #"%" used to find the remainder of the division
print("Leftover slices:", Leftover_slices, "slices\n")

asteroid_sizes = [34, 7, 108, 55, 2, 89]
smallest = min(asteroid_sizes)
largest = max(asteroid_sizes)
print("Smallest asteroid:", smallest)
print("Largest asteroid:", largest)

