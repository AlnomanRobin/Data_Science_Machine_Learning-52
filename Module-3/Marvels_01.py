# Introducing a method
class Avenger:
    def introduce(self, name): #parameterized method
        print(f"I am {name}, and I protect the world!")


ironman = Avenger()
ironman.introduce("Iron Man")

hulk = Avenger()
hulk.introduce("Hulk")