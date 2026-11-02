class Grandpa:
    def advice(self):
        print("Never ignore bugs in your code!")

class Father(Grandpa):
    def teach(self):
        print("Teaxhing JavaScript")

class Son(Father):
    pass

karim = Son()
karim.advice()
karim.teach()
print("\n")
#Multiple Inheritance
class Mother:
    def discipline(self):
        print("Go to bed at 10 PM!")

class Uncle:
    def math(self):
        print("Solving Equations....")

class daughter(Mother, Uncle):
    pass
ayesha = daughter()
ayesha.discipline()
ayesha.math()