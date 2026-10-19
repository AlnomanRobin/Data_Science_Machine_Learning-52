# Define a class that represents an Avenger.
class Avenger:
    # This method displays the Avenger's fighting action.
    def fight(self):
        print("Avenger is fighting!")

# Create an Iron Man object and call its fight method.
ironman = Avenger()
ironman.fight()

# Create a Hulk object and call the same method.
hulk = Avenger()
hulk.fight()

# Display a final message after both Avengers are ready.
print("Ironman and Hulk are ready to fight!")
