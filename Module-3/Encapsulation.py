class family:
    def __init__(self):     # constructor def__init__
        self.secret_fund=5000

    def get_fund(self):     # getter method
        return self.secret_fund    

dad=family()     # object creation
print(dad.secret_fund)     # accessing the getter method

print("\n\n")

class fund:
    def __init__(self):
        self.__secret_fund=5550 # private attribute

    def get_fund(self):     
        return self.__secret_fund    # getter method

dad=fund()     # object creation
#print(dad.__secret_fund)     # accessing the getter method
print(dad.get_fund())     # accessing the getter method
