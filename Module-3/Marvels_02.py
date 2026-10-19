# Default constructor
class Avenger:
    def __init__(self):
        self.name = "Sunny"

    def introduce(self):
        print(f"I am {self.name}, and I know data science")


captain = Avenger()
captain.introduce()
print("\n")

class A:
    def __init__(self):
        self.name = "Elizabeth"

    def introduce(self, skills):
        print(f"I am {self.name}, and I know {skills}")

B=A()
B.introduce("AI")