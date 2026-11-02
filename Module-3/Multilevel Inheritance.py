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
