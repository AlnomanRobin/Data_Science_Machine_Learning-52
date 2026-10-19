#Inheritance in Python
class Hero:
    def protect(self):
        print("Protecting the world!")

class IronMan(Hero):
    def fly(self):
        print("Flying in the sky!")

tony = IronMan()
tony.protect()  # Inherited method
tony.fly()      # Own method