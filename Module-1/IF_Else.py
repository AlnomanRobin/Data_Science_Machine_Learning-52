a=13
b=10
if a > b:
    print("a is greater than b")
else:
    print("a is not greater than b")

x=20
y=20
if x > y:  #if — When a condition is true
    print("x is greater than y")
elif x < y: #elif — When the previous condition is false and this condition is true
    print("x is less than y")
else:      #When all the previous conditions are false
    print("x is equal to y")


# and: both conditions must be true
age = 25
has_id = True
if age >= 18 and has_id:
    print("You can enter")

# or: at least one condition must be true
day = "Friday"
if day == "Friday" or day == "Saturday":
    print("It is the weekend")

# not: reverses the result of a condition
is_raining = False
if not is_raining:
    print("You do not need an umbrella")

print("\n") #For New Line
a = 200
b = 33
c = 50

if a > b or c > a:
    print("Both conditions are true")


# Nested if
Z = 12
if Z > 10:
    print("Above Ten")
    if Z > 20:
        print("and also above 20")
    else:
        print("but not above 20")

if b>a:
    pass





    