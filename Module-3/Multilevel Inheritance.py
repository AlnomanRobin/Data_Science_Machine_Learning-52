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

print("\n")

#Method overloading
class ReportCard:
    def marks(self, math=None, english=None):
        if math is not None and english is not None:
            print(f"Math: {math}, English: {english}")
        if math is not None:
            print(f"Math: {math}")
        else:
            print("No marks provided.")
karim_report = ReportCard()
karim_report.marks(90, 85)