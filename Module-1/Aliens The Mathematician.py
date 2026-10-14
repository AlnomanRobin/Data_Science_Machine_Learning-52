import math

distance_to_home = 384400
gravity = 9.8
thrust_needed = math.sqrt(gravity * distance_to_home) #square root = math.sqrt
print("Thrust needed:", thrust_needed)
print("Thrust needed:", round(thrust_needed, 2)) #round to 2 decimal places
print("\n")

base_length = 10
height = 15
area = 0.5 * base_length * height
print("area: ", area)
angle_radians = math.atan(height / base_length) #arctangent = math.atan
angle_degree = math.degrees(angle_radians)
print("Angle:", round(angle_degree, 2), "degrees")
print("\n")

test_value = 5.87
up_value = math.ceil(test_value)
print(up_value)

down_value = math.floor(test_value)
print(down_value)

round_value = round(test_value)
print(round_value)

