tweet = "Hello earth, sunny here reporting from sector 9"

print("Start of tweet:", tweet[0:5])
print("Start of tweet:", tweet[:5])
print("End of tweet:", tweet[-7:])
print("Middle of tweet:", tweet[25:38])

print("Total characters:", len(tweet))
print("Total characters without spaces:", len(tweet.replace(" ", "")))
print("Tweet without spaces:", tweet.replace(" ", ""))

print("Total words:", len(tweet.split()))   # "Hello","earth,","sunny","here","reporting","from","sector","9"
print("Tweet without e:", tweet.replace("e", ""))   # "Hello","earth,","sunny","here","reporting","from","sector","9"
print("Every word starts with a capital letter:", tweet.title())

print("Tweet in uppercase:", tweet.upper())
print("Tweet in lowercase:", tweet.lower())
print("Tweet with swapped case:", tweet.swapcase())

print("Tweet with replaced words:", tweet.replace("sunny", "stormy").replace("sector 9", "sector 7"))
print(len(tweet))
print("\n")

messy = "Visit###Earth!! It's#sooooooo!!#green###"
cleaned = messy.replace("#", "").replace("!", "").replace("sooooooo", "so")
print("Cleaned text:", cleaned)
print("Capitalized:", cleaned.capitalize())
print("Upper case:", cleaned.upper())
print("Lower case:", cleaned.lower())
print("\n")

planet = "Earth"
temperature = 22.56789
weather = "mild"
report = "Planet: {}, Temp: {:.2f} degree C, weather: {}".format(planet, temperature, weather)  # Temp: {:.2f}=> 2 decimal places
print(report)   #Temp: {}=> placeholder for the value
print("\n")

#new way of formatting strings using f-strings
distance = 384400.26874
unit = "km"
message = f"Distance to Moon from Earth: {distance:.2f} {unit}"
print(message)
print("\n")

fruits = ["Apple", "Mango", "Banana"]
fruits.append("Orange") # append() method adds an item to the end of the list
fruits[0] = "Grapes"
print(fruits)
