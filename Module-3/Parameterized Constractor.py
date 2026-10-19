# Parameterized Constructor in Python
class Avenger:
    def __init__(self, name, power):
        self.name = name
        self.powerfull = power

    def show(self):
        print(f"Name: {self.name}, Power: {self.powerfull}")

spider = Avenger("Spider Man", "Web Slinging")
spider.show()